#summer movie budget stuff
rm(list = ls(all = TRUE)) #clear workspace
setwd("/Users/QuoctrungBui/cinebudgets/")
library('reshape')
library('ggplot2')
require(RSvgDevice)

budget <- read.table("movie-budgets.csv", header = T, sep = "|", na.strings = "NA", quote = "",
                     fileEncoding="latin1", fill = TRUE)

budget$date <- as.character(budget$date)
budget$date <- as.Date(budget$date, "%m/%d/%Y")
budget$month <- format(budget$date,"%m")
budget$month <- as.numeric(budget$month)
budget$year <- format(budget$date,"%Y")
budget$year <- as.numeric(budget$year)

#inflation
cpi <- read.table("cpi-y.csv", header = T, sep = ",", na.strings = "NA", quote = "",
                  fileEncoding="latin1", fill = TRUE)
cpi[,2] <- 100*(cpi[,2]/cpi[67,2])
budget<- merge(budget,cpi,by.id="year")

#deflate
budget$intl.r <- budget$intl/budget$cpi
budget$domestic.r <- budget$domestic/budget$cpi
budget$budget.r <- budget$budget/budget$cpi

#other transforms
budget$intlact <- budget$intl-budget$domestic
budget$intratio <- budget$domestic/budget$intl
budget$profit <- budget$intl-budget$budget
budget$domprofit <- budget$domestic-budget$budget
budget$intlprofit <- budget$intl-budget$budget

#summer movies
budget.summer <- budget[which(budget$year>=1995 & budget$month>=5 & budget$month<=9),]
qplot(budget.summer$budget, budget.summer$intl)
qplot(budget.summer$date, budget.summer$intratio)

#most profitable movie? still missing Avatar
ggplot(budget.summer, aes(date, profit, label=name)) + geom_point(size=1) + geom_text(data = subset(budget.summer, abs(profit) > 100000000), vjust=0, size=3)
#what if we only measured domestic revenue? 
ggplot(budget.summer, aes(date, domprofit, label=name)) + geom_point(size=1) + geom_text(data = subset(budget.summer, abs(domprofit) > 100000000), vjust=0, size=3)
ggplot(budget.summer, aes(date, intlprofit, label=name)) + geom_point(size=1) + geom_text(data = subset(budget.summer, abs(intlprofit) > 100000000), vjust=0, size=3)
ggplot(budget.summer, aes(month, domprofit, label=name)) + geom_point(size=1) + geom_text(data = subset(budget.summer, abs(domprofit) > 100000000), vjust=0, size=3)
ggplot(budget.summer, aes(month, intlprofit, label=name)) + geom_point(size=1) + geom_text(data = subset(budget.summer, abs(intlprofit) > 100000000), vjust=0, size=3)

ggplot(budget.summer, aes(date, domestic, label=name)) + 
  geom_point(size=1) + 
  geom_text(data = subset(budget.summer, abs(intl) > 100000000), vjust=0, size=3) + 
  stat_smooth(method = "lm", formula = y ~ x, size = 1) 


ggplot(budget.summer, aes(date, intl, label=name)) + 
  geom_point(size=1) + 
  geom_text(data = subset(budget.summer, abs(intl) > 100000000), vjust=0, size=3) + 
  stat_smooth(method = "lm", formula = y ~ x, size = 1) 

ggplot(budget.summer, aes(date, intlact, label=name)) + 
  geom_point(size=1) + 
#   geom_text(data = subset(budget.summer, abs(intlact) > 100000000), vjust=0, size=3) + 
  stat_smooth(method = "lm", formula = y ~ x, size = 1) 

