#!/bin/bash
#SBATCH --partition=queue
#SBATCH --time=14-00:00:00
#SBATCH -N 1 # Nodes
#SBATCH -n 1 # Tasks
#SBATCH --cpus-per-task=10
#SBATCH --error=prokka.%J.err
#SBATCH --output=prokka.%J.out
#SBATCH --mail-user=samche42@gmail.com
#SBATCH --mail-type=ALL

cd /home/sam/Stromatolite_Project/All_manually_curated/Genomes

for genome in `ls *.fasta`
do
        /home/sam/miniconda3/bin/prokka \
        --compliant --centre UoN --outdir /home/sam/Stromatolite_Project/All_manually_curated/Genomes/${genome/.fasta/''} \
        --locustag ${genome/.fasta/''} --prefix ${genome/.fasta/''} ${genome}
done
