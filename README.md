# Strom_Brief_report
Raw data, scripts and descriptions of figure creation for manuscript

Creating Figs. 1, 5 and 6

a. Count gene occurence in KEGG annotations using kegg_parser.py. This finds the number of times a given KO annotation occurs per genome.
b. Count gene occurence in prokka annotations using prokka_parser.py. This finds the number of times a given prokka annotation occurs per genome.
c. Add prokka and KEGG counts together and divide by two to find the average.
d. Multiply counts by bin coverage. The more abundant the genome, the more abundant are it's genes. Coverage is a proxy for abundnace.
e. Divide by weighted sample coverage (calculated by weighted_contig_coverage_calculator.py) so that we can compare abundances between samples.

