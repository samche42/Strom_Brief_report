Creating heatmap from KO data

library(tidyr)
library(ggplot2)
library(viridis)
 
mine.data <- read.csv(file = "Leftover_sample_KO_heatmap_log.txt", header=T, sep="\t")
mine.long <- gather(data = mine.data, key = Class, value = Abundance, -c(1))
mine.long$Genome <- factor(mine.long$Genome, levels = unique(mine.long$Genome))

t <- ggplot(data = mine.long, mapping = aes(x = Class, y = Genome, fill = Abundance),fill = "transparent") +
geom_tile() +
xlab(label = "Site") + xlab(label = "Function") +
scale_fill_viridis(option="magma", direction=-1, limits=c(0, 0.04)) +
theme(axis.text.y = element_text(size = 10, color="black"), 
axis.text.x = element_text(angle=90, hjust=1, size =10, color="black"), 
axis.title.x =element_text(size=10, color="black"), 
axis.title.y =element_text(size=10, color ="black"),
panel.background = element_rect(fill = "transparent"),
plot.background = element_rect(fill = "transparent"), 
panel.grid.major = element_blank(),
panel.grid.minor = element_blank())
t
