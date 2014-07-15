rm(list = ls(all = TRUE)) #clear workspace
setwd("/Users/QuoctrungBui/cinebudgets/")
library('reshape')
library('ggplot2')
require(RSvgDevice)

budget <- read.table("movie-budgets.csv", header = T, sep = "|", na.strings = "NA", quote = "",
                   fileEncoding="latin1", fill = TRUE)

cine <- read.table("new_mdata.htm.csv", header = T, sep = "|", na.strings = "NA", quote = "",
                   fileEncoding="latin1", fill = TRUE)

cine.small <- unique(cine[,c(1:5)])
combined <- merge(cine.small,budget, by.id = "name")

cine.small.lee <- cine[which(cine$director=="Ang Lee" & cine$name=="Brokeback Mountain"),]
hist(cine.small.lee$shotlength)
# one_ob <- combined[!duplicated(combined$name),]
directors<-unique(cine$director)

cine.small.scott <- cine[which(cine$director=="Ridley Scott"),]
Ridley Scott

cine.small.lee <- cine[which(cine$director=="Michael Ba")
cine.small.tarantino <- cine[which(cine$director=="Quentin Tarantino" & cine$name == "Kill Bill: Vol. 2"),]
                             
# Quentin Tarantino

qplot(combined$budget,combined$asl)
# qplot(data = combined, aes(x=asl,y=budget,label=name)) + geom_point() +  geom_text(angle=45)
