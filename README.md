# CHERRY-crispr version


CHERRY is a python library for predicting the interactions between viral and prokaryotic genomes. CHERRY is based on a deep learning model, which consists of a graph convolutional encoder and a link prediction decoder.


In this program, we provide an extension version of CHERRY, which uses the CRISPR information in CHERRY's database for multi-host (host range) prediction. 

```

Input (provided by the user):
    1. phage contigs from their samples (FASTA files)

Output:
    The host range of the given phages (CSV files)
```


## Required Dependencies

* Python 3.x
* Pandas
* Numpy
* Biopython
* NCBI BLAST+

## An easiler way to install

We suggest you to install all the package using conda (both miniconda and Anaconda are ok) following the command lines as below:

```
conda create --name cherry_crispr_multihost python=3.8
conda activate cherry_crispr_multihost

conda install pandas numpy biopython
conda install blast -c bioconda
```

## Usage

Once install the required environment, you need to activate it when you want to use:

```
conda activate cherry_crispr_multihost
```

Then, the command of multi-host extension can be called by:


```
python PATH_TO_cherry_crispr_multihost/Cherry_multihost.py --infile PATH_TO_FASTA --outfolder PATH_TO_OUTPUT_FOLDER --datasetpth [where you place the dataset folder provided in this GitHub] --threads NUM_OF_THREAD --ident IDENTITY_OF_ALIGNMENT --coverage COVERAGE_OF_ALIGNMENT

# example
python CHERRY_crispr_multihost/Cherry_multihost.py --infile nucl.fasta --outfolder test_out/ --datasetpth CHERRY_crispr_multihost/dataset --ident 75 --coverage 0.75
```


There are two thresholds for users:

1. --ident: the identity of the CRISPRs alignments (default: 75)
2. --coverage: the coverage of the CRISPRs alignments (default: 0.75)


## Outputs

There are two output files in `--outfolder PATH_TO_OUTPUT_FOLDER`.

1. alignment_result.tab: BLASTN results between CRISPR and phage
2. prediction.csv: CSV files of the prediction (alignment > `--ident IDENTITY_OF_ALIGNMENT` && > `--coverage COVERAGE_OF_ALIGNMENT`)



## Citation
If you use this program, please cite the following papers:

* CHERRY:
```
Jiayu Shang, Yanni Sun, CHERRY: a Computational metHod for accuratE pRediction of virus–pRokarYotic interactions using a graph encoder–decoder model, Briefings in Bioinformatics, 2022;, bbac182, https://doi.org/10.1093/bib/bbac182
```

The original version of CHERRY can be found via: [CHERRY](https://github.com/KennthShang/CHERRY)

