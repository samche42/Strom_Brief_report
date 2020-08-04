import os
from Bio import SeqIO
import sys
from csv import DictWriter

input_directory = sys.argv[1]

#create list of fasta files to parse through
sample_files = [file for file in os.listdir(input_directory) if file.endswith(".fasta")]
headers_list = []
for sample in sample_files:
        total_length = 0
        sample_weight = 0
        headers = list(r.id for r in SeqIO.parse(os.path.join(input_directory,sample), "fasta"))
        #Find sum of all contig lengths
        for header in headers:
                length = float(header.split('_')[3])
                total_length = total_length + length
        #Find length weighted average coverage for sample
        for head in headers:
                length = float(header.split('_')[3])
                coverage = float(header.split('_')[5])
                contig_weight = (length/total_length)*coverage
                sample_weight = sample_weight + contig_weight
        print(str(sample)+" : "+str(sample_weight))
