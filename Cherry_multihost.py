import os
import sys
import Bio
import logging
import argparse
import subprocess
import scipy as sp
import numpy as np
import pandas as pd
import pickle as pkl
import networkx as nx
import scipy.stats as stats
import scipy.sparse as sparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Blast.Applications import NcbiblastnCommandline


parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--infile', type=str, default = 'virus.fa')
parser.add_argument('--outfolder', type=str, default = 'out')
parser.add_argument('--datasetpth', type=str, default = 'dataset')
parser.add_argument('--threads', type=float, default = 16)
parser.add_argument('--ident', type=float, default = 0.75)
parser.add_argument('--coverage', type=float, default = 0.75)
inputs = parser.parse_args()

datasetpth = inputs.datasetpth
infile     = inputs.infile
outfolder  = inputs.outfolder
coverage_in   = inputs.coverage
ident_in      = inputs.ident
threads       = inputs.threads

def check_folder(file_name):
    if not os.path.exists(file_name):
        _ = os.makedirs(file_name)
    else:
        print("folder {0} exist... cleaning dictionary".format(file_name))
        if os.listdir(file_name):
            try:
                _ = subprocess.check_call("rm -rf {0}".format(file_name), shell=True)
                _ = os.makedirs(file_name)
                print("Dictionary cleaned")
            except:
                print("Cannot clean your folder... permission denied")
                exit(1)

check_folder(outfolder)

################################################################################
###############################  Run CRISRP   ##################################
################################################################################

query_file = f"{infile}"
db_host_crispr_prefix = f"{datasetpth}/crispr_db/allCRISPRs"
output_file = f"{outfolder}/alignment_result.tab"
bacteria_df = pd.read_csv(f'{datasetpth}/prokaryote.csv')
crispr_call = NcbiblastnCommandline(query=query_file,db=db_host_crispr_prefix,out=output_file,outfmt="6 qseqid sseqid evalue pident length slen", evalue=1,gapopen=10,penalty=-1,
                                  gapextend=2,word_size=7,dust='no',
                                 task='blastn-short',perc_identity=90,num_threads=threads)
crispr_call()


crispr_pred = {}
with open(output_file) as file_out:
    for line in file_out.readlines():
        parse = line.replace("\n", "").split("\t")
        virus = parse[0]
        prokaryote = parse[1].split('|')[1]
        prokaryote = prokaryote.split('.')[0]
        ident = float(parse[-3])
        length = float(parse[-2])
        slen = float(parse[-1])
        if length/slen > coverage_in and ident > ident_in:
            try:
                crispr_pred[virus].append(prokaryote)
            except:
                crispr_pred[virus] = [prokaryote]

with open(f'{outfolder}/prediction.csv', 'w') as f_out:
    f_out.write(f'Accession,Host_range\n')
    for virus in crispr_pred:
        results = f'{virus},'
        for host in crispr_pred[virus]:
            try:
                name = bacteria_df[bacteria_df['Accession'] == host]['Species'].values[0]
                results += f'{name}({host})｜'
            except:
                results += f'({host})｜'
        results = results[:-1]+'\n'
        f_out.write(f'{results}')

os.system(f"sed -i '1i\qseqid\tsseqid\tevalue\tpident\tlength\tslen' {outfolder}/alignment_result.tab")

print('Program complete!')


