# Ejemplo Regresión lineal

# eq general para regresión lineal y = ax + b
# y variable dependiente o respuesta
# x variable independiente o predictora
# a,b constantes llamadas coeficientes

# Valores altura en cm
x <- c(158, 170, 142, 182, 127, 130, 181, 166, 157, 134, 175)

# valores peso en kg
y <- c(65, 79, 58, 91, 45, 59, 77, 73, 60, 51, 90)

# Función lm(formula, data) (linear models)
# formula representa la relación entre x y
# data vector al cual se aplicará la formula

# Aplicamos formula
relacion <- lm(y~x)
print(summary(relacion))

# usamos la funcion predict() para realizar inferencias con nuevos datos
# predict(object, newdata)
# object es la formula o modelo creado por la función lm()
# newdata es unv ector que contengalos nuevos valores

newData <- data.frame(x = 200)
resultado <- predict(relacion, newData)
print(resultado)

# Visualizamos nuestro modelo en una gráfica
png(file = "linearregression.png")
plot(y,x,col = "red",main = "Regresión lineal con Altura & Peso",
     abline(lm(x~y)),cex = 1.3,pch = 16,xlab = "Peso [kg]",ylab = "Altura [cm]")

# Save the file.
dev.off()


