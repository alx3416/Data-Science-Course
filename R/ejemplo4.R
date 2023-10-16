library(DescTools)

#Obtener tendencias centrales
b <- c(3,4,5,6,12,12)
print(sum(b))
print(mean(b))
print(median(b))

#obtener medidas dispersion
print(var(b))
print(sd(b))
moda <- Mode(b)
print(moda)

# install.packages("DescTools")

x <- matrix(1:9, 3, 3)
print(x)
print(colMeans(x))
print(rowMeans(x))

# cuartiles y percentiles
res<-quantile(b, probs = c(0,0.25,0.5,0.75,1))
print(res)
res<-quantile(b, probs = c(0.33,0.66))
print(res)

# Vamos a crear distribucion normal
y <- rnorm(100)

# nombre de la imagen
png(file = "figura5.png")
hist(y, main = "Distribución Normal", prob=TRUE)
curve(dnorm(x,mean=mean(y),sd=sd(y)), add=TRUE,col="red")
abline(v=quantile(y, .25), col='blue', lwd=3)
abline(v=quantile(y, .75), col='blue', lwd=3)
abline(v=quantile(y, .50), col='green', lwd=3)
# Guardamos el archivo
dev.off()


