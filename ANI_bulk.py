#!/usr/bin/env python

# Program to make a all-v-all matrix of ANI values when given an arbitrary number of fasta files
# Note: uses the ANIcalculator program (https://ani.jgi-psf.org/html/download.php), and
# expects nucleotide fasta files of the protein coding genes only.
# If you annotate a genome with prokka, then the *.ffn file will contain tRNA and rRNA as well.
# To get just the protein coding genes:
# 	grep ">" PROKKA_****.faa | sed 's/^.//' | cut -f 1 -d ' ' > proteins.list
#   extract_fasta.py PROKKA_****.ffn proteins.list PROKKA_****_only_protein_coding.fasta

import argparse
import os
import itertools

parser = argparse.ArgumentParser(description="Calculate ANI for all possible pairs of a list of nucleotide fasta files")

parser.add_argument('-f','--fasta_list', metavar="<fasta_list>", help='Path to list of fasta paths', required=True)
parser.add_argument('-o','--output_dir', metavar="<dir>", help='Path to output directory', required=True)

args = vars(parser.parse_args())

fasta_list_path = args['fasta_list']
output_dir_path = args['output_dir']

# We have to create the output dir if it doesn't exist
if not os.path.isdir(output_dir_path):
	os.makedirs(output_dir_path)

# First parse the input path list
fasta_paths = list()
species_name_list = list()

with open(fasta_list_path) as fasta_list:
	for line in fasta_list:
		fasta_paths.append(line.rstrip())
		species_name_list.append('.'.join(line.rstrip().split('.')[:-1]))

# Initialize a matrix which will hold the results
ANI_matrix = list()
for i in range(len(fasta_paths)):
	row = [None] * len(fasta_paths)
	ANI_matrix.append(row)

# Initialize a matrix which will hold the results
AF_matrix = list()
for i in range(len(fasta_paths)):
	row = [None] * len(fasta_paths)
	AF_matrix.append(row)

# Now we need to get all possible combinations of two indices in the range len(fasta_paths)
combination_tuples = list(itertools.combinations(range(len(fasta_paths)), 2))

# Now we do the ANI calculations
for combination in combination_tuples:
	index1 = combination[0]
	index2 = combination[1]
	fasta_path1 = fasta_paths[index1]
	fasta_path2 = fasta_paths[index2]

	ANI_command = '/home/sam/Tools/ANIcalculator_v1/ANIcalculator -genome1fna ' + fasta_path1 + ' -genome2fna ' + fasta_path2 + ' -outfile ' + output_dir_path + '/ANI_output'
	print(ANI_command)
	os.system(ANI_command)

	# Parse output
	output = open(output_dir_path + '/ANI_output',"r+")
	output_lines = output.readlines()
	output.close()

	ANI1 = float(output_lines[1].split('\t')[2])
	ANI2 = float(output_lines[1].split('\t')[3])
	ANI_mean = (ANI1 + ANI2) / 2

	AF1 = float(output_lines[1].split('\t')[4])
	AF2 = float(output_lines[1].split('\t')[5].rstrip('\n'))
	AF_mean = (AF1 + AF2) / 2
	# Store ANI value
	ANI_matrix[index1][index2] = ANI_mean
	ANI_matrix[index2][index1] = ANI_mean

	# Store AF value
	AF_matrix[index1][index2] = AF_mean
	AF_matrix[index2][index1] = AF_mean

	# Cleanup
	os.system('rm ' + output_dir_path + '/ANI_output')

# Now we output the Averager Nucleotide index matrix to a file
output = open(output_dir_path + '/ANI_matrix', 'w')
header_line = '\t' + '\t'.join(species_name_list) + '\n'
output.write(header_line)

for i in range(len(ANI_matrix)):
	new_list = list()
	for j in range(len(ANI_matrix[i])):
		if ANI_matrix[i][j] == None:
			new_list.append('-')
		else:
			new_list.append(str(ANI_matrix[i][j]))
	current_line = species_name_list[i] + '\t' + '\t'.join(new_list) + '\n'
	output.write(current_line)

output.close()

# Now we output the Alignment fraction matrix to a file
output = open(output_dir_path + '/AF_matrix', 'w')
header_line = '\t' + '\t'.join(species_name_list) + '\n'
output.write(header_line)

for i in range(len(AF_matrix)):
	new_list = list()
	for j in range(len(AF_matrix[i])):
		if AF_matrix[i][j] == None:
			new_list.append('-')
		else:
			new_list.append(str(AF_matrix[i][j]))
	current_line = species_name_list[i] + '\t' + '\t'.join(new_list) + '\n'
	output.write(current_line)

output.close()
