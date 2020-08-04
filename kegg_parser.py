#This script can be used to count the number of times a particluar set of KO entries 
#appears in n genomes. List of KOs needs one KO entry per line and output from kofamscan. 
#Script will output KO counts in a table. Example KO list in git repo "Nitrogen_list"

#Usage: python3 kegg_parser.py path/to/kofamsccan/output Query_list

import os
import sys
from csv import DictWriter

input_directory = sys.argv[1]

query = sys.argv[2] #Custom list of KOs to be checked

query_list = []
with open(os.path.join(input_directory, query)) as query_input:
        for line in query_input:
                query_list.append(line.strip("\n"))

#create list of kegg files to parse through
kegg_files = [file for file in os.listdir(input_directory) if file.endswith(".KEGG.Output")]

#create dictionary to store genome kegg annotations
kegg_annotations = {}
ko_list = []
#Create a dictionary for each genome, with all query KOs set to a count of 0.
for kegg in kegg_files:
        ko_entries = []
        genome_dict = {"Genome": str(kegg)}
        for ko in query_list:
                genome_dict[ko] = 0

#Open the kegg file and count the number of occurances of each key in the genome dictionary
        file = open((os.path.join(input_directory, kegg)), 'r').read()
        for key, value in genome_dict.items():
                if str(key) == "Genome":
                        pass
                else:
                        genome_dict[key] = file.count(str(key))
        ko_list.append(dict(genome_dict)) #Append new dictionary to overall list

#Write it out to a file
keys = ko_list[0].keys()
with open((os.path.join(input_directory,"KEGG_annotation_count_table.txt")),"w") as output:
        dict_writer = DictWriter(output, keys, delimiter = "\t")
        dict_writer.writeheader()
        for item in ko_list:
                dict_writer.writerow(item)
output.close()
