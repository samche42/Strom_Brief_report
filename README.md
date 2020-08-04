# Strom_Brief_report
Raw data, scripts and descriptions of figure creation for manuscript


Genome gene abundnace (e.g. count occurance of phoX in genome bin CSU_1_1) - Used to create Figs. 1, S5 and S6

a. Count gene occurence of KEGG annotations per genome using kegg_parser.py. 

b. Count gene occurence of prokka annotations per genome using prokka_parser.py. 

c. Add prokka and KEGG counts together and divide by two to find the average.

d. Multiply counts by weighted genome coverage (calculated by weighted_contig_coverage_calculator.py) so that we can compare abundances between samples.


Sample gene abundance (e.g. count occurance of phoX in CSU_Bacteria.faa) - used to create Fig. S3

a. Count gene occurence of KEGG annotations per Bacteria.faa file using kegg_parser.py. 

b. Count gene occurence of prokka annotations per Bacteria.faa using prokka_parser.py. 

c. Average gene count = (Prokka count + KEGG count)/2

d. Weighted sample coverage was calculated by weighted_contig_coverage_calculator.py

e. Sample gene abundance = Average gene count * Weighted sample coverage


Total gene abundance (e.g. count of ALL genes in CSU_Bacteria.fasta)

a. Total genes were counted per sample: (for faa in `ls *.faa`; do echo ${faa}; grep ">" ${faa} | wc -l; done). This was performed for all Bacteria.faa files.

b. Sample weighted coverages were calculated using weighted_contig_coverage_calculator.py with Bacteria.fasta files

c. Total gene abundance per sample = gene count x sample weighted coverage.



Finding relative percentage:

Figs. 1, S5 and S6:

Relative percentage = Genome gene abundance / Total gene abundance *100

Fig. S3

Relative percentage = Sample gene abundance / Total gene abundance *100

All scripts used here are in the repo, as well as a master Excel file with all metadata and calculations.

Additionally, I have uploaded a compressed folder of all prokka and kofamscan output files, and the scripts used to run these tools for reproducibility. 
