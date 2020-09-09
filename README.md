# Strom_Brief_report
Raw data, scripts and descriptions of figure creation for manuscript

##KEGG Query genes

Genes in query files were collected manually from KEGG systems and literature review. Both key gene query files and the photosynthesis query files are in this repo. 

##Total gene count:

a. Total genes were counted per sample: (for faa in `ls *.faa`; do echo ${faa}; grep ">" ${faa} | wc -l; done). This was performed for all Bacteria.faa files.

##Genome gene abundance (e.g. count occurance of phoX in genome bin CSU_1_1) - Used to create Figs. 1, S5 and S6

a. Count gene occurence of KEGG annotations per genome using kegg_parser.py. 

b. Divide count by total number of genes in sample, and multiply by 100 to get relative percentage (e.g. CRU_1_1 phoX count = 3, CRU total gene count = 30000 : 3/30000 x 100 = 0.01%)

##Sample gene abundance (e.g. count occurance of phoX in CSU_Bacteria.faa) - used to create Fig. S3

a. Count gene occurence of KEGG annotations from Bacteria.faa files using kegg_parser.py. 

*Note Bacteria.faa files include all unclustered and small (< 3000 bp) contigs.

b. Divide count by total number of genes in sample, and multiply by 100 to get relative percentage (e.g. CRU phoX count = 30, CRU total gene count = 30000 : 30/30000*100 = 0.1%)

c. The relative percentage of genes (Fig. S3B) that were annotated but not clustered were calculated by:

Remaining genes rel perc = Total annotated geneX abundance in sample Y - sum (gene X abundance in all genomes binned from sample Y)

##Data availability

Additionally, if you would like access to kofamscan, prokka, prodigal and/or Autometa output please do not hesitate to contact me at either swaterworth@wisc.edu or samche42@gmail.com (both are checked multiple times a day) and I will happily send any and all files you require. 
