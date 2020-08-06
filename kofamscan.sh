#!/bin/bash
#SBATCH --partition=queue
#SBATCH --time=14-00:00:00
#SBATCH -N 1 # Nodes
#SBATCH -n 1 # Tasks
#SBATCH --cpus-per-task=6
#SBATCH --error=kofam.%J.err
#SBATCH --output=kofam.%J.out
#SBATCH --mail-user=samche42@gmail.com
#SBATCH --mail-type=ALL

cd /home/sam/T.favus_Project/All_man_curated_updated

for protein_file in `ls *.faa`; do
        /home/evan/tools/programs_3rd_party/kofamscan/kofamscan ${protein_file} \
        --cpu 10 \
        -o ${protein_file/.faa/_kegg_output} \
        -p /home/evan/tools/programs_3rd_party/kofamscan/db/profiles \
        -k /home/evan/tools/programs_3rd_party/kofamscan/db/ko_list \
        -f mapper
done
