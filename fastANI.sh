#!/bin/bash
#SBATCH --partition=queue
#SBATCH --time=14-00:00:00
#SBATCH -N 1 # Nodes
#SBATCH -n 1 # Tasks
#SBATCH --cpus-per-task=10
#SBATCH --error=bulk_ANI.%J.err
#SBATCH --output=bulk_ANI.%J.out
#SBATCH --mail-user=samche42@gmail.com
#SBATCH --mail-type=ALL

python /home/sam/Useful_little_scripts/scripts/ANI_bulk.py \
-f /home/sam/Stromatolite_Project/All_manually_curated/Genomes \
-o /home/sam/Stromatolite_Project/All_manually_curated/Genomes
