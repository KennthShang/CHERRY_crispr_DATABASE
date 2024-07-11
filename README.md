![CHERRY](imgs/logo.png)

# CHERRY-crispr DATABASE version

This program provides an extension version of CHERRY, which uses the CRISPR information in CHERRY's database for host prediction. 

The main local program is available via [PhaBOX](https://github.com/KennthShang/PhaBOX) and [WebServer](https://phage.ee.cityu.edu.hk/)


Table of Contents
=================
* [ 🚀&nbsp; Installation](#install)
* [ 🚀&nbsp; Quick Start](#quick)
* [ ⌛️&nbsp; Usage](#usage)
* [ 📈&nbsp; Output Format  ](#output)
* [ 📫&nbsp; Have a question? ](#question)
* [ ✏️&nbsp; Citation ](#citation)
* [ 🤵&nbsp; Team ](#team)


<a name="install"></a>
## 🚀&nbsp; Installation

**If you have already installed phabox before, you can skip this part and directly use the phabox environment**


We suggest you install all the packages using conda (both Miniconda and Anaconda are ok) following the command lines below:

```
conda create --name cherry_crispr_db python=3.8
conda activate cherry_crispr_db
conda install pandas numpy biopython
conda install blast -c bioconda
```



<a name="quick"></a>
## 🚀&nbsp; Quick Start

```
git clone https://github.com/KennthShang/CHERRY_crispr_DB.git

python CHERRY_crispr_DB/Cherry_crispr_db.py --infile nucl.fna --outfolder test_out/ --datasetpth CHERRY_crispr_DB/dataset --ident 95 --coverage 0.95

```


<a name="usage"></a>
## ⌛️&nbsp; Usage 


      --infile 
                            input fasta file
      --outfolder 
                            path to the output folder
      --datasetpth 
                            path to the CHERRY_crispr_DB/dataset/
      --threads 
                            Number of threads to run the program (default 8)
      --ident
                            Identity threshold for the alignments (default 95)
      --coverage
                            Coverage threshold for the alignments (default 0.95)


**The program will return the results that meet both ident & coverage thresholds.**



<a name="output"></a>
## 📈&nbsp; Output format

```
Input (provided by the user):
    1. phage contigs from their samples (FASTA files)

Output:
    1. The host range of the given phages (CSV files)
    2. RAW BLASTN alignment results (NCBI blast+)
```


<a name="question"></a>
## 📫&nbsp; Have a question?

We are happy to hear your question on our issues page [CHERRY](https://github.com/KennthShang/CHERRY_crispr_DB/issues)! Obviously, if you have a private question or want to cooperate with us, you can always **reach out to us directly** via our email: jiayushang@cuhk.edu.hk 


<a name="citation"></a>
## ✏️&nbsp; Citation
If you use this program, please cite the following papers:

* CHERRY:
```
Jiayu Shang, Yanni Sun, CHERRY: a Computational metHod for accuratE pRediction of virus–pRokarYotic interactions using a graph encoder–decoder model, Briefings in Bioinformatics, 2022;, bbac182, https://doi.org/10.1093/bib/bbac182
```


<a name="team"></a>
## 🤵&nbsp; Team

 * <b>Head of PhaBOX program</b><br/>

 | [Jiayu SHANG](https://kennthshang.github.io/)       | [Cheng PENG](https://github.com/ChengPENG-wolf)       |
|:-------------------------:|:-------------------------:|
| <img width=120/ src="imgs/mine.pic.jpg?raw=true"> | <img width=120/ src="imgs/Wolf.jpg?raw=true"> |


 * <b>Supervisor</b><br/>
 
 | [Yanni SUN](https://yannisun.github.io/)       |
|:-------------------------:|
| <img width=120/ src="imgs/yanni.png?raw=true"> |


Our groupmates also provide many useful tools for bioinformatics analysis. Please check [Yanni's Group](https://yannisun.github.io/tools.html) for further information. Hope you will like them! 

