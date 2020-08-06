 #!/bin/bash
#SBATCH --partition=queue
#SBATCH --time=14-00:00:00
#SBATCH -N 1 # Nodes
#SBATCH -n 1 # Tasks
#SBATCH --cpus-per-task=6
#SBATCH --error=joly.%J.err
#SBATCH --output=joly.%J.out
#SBATCH --mail-user=samche42@gmail.com
#SBATCH --mail-type=ALL
 
 JolyTree.sh  -i /home/sam/Stromatolite_Project/All_manually_curated/Genomes  -b Key_gene  -k 10000
