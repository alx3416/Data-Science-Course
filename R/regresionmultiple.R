# Regresión múltiple
# ejemplo con dataset diabetes, fuente: https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html

#Importar datos
input <- read.delim("https://www4.stat.ncsu.edu/~boos/var.select/diabetes.rwrite1.txt", 
                     header = TRUE, sep = " ", dec = ".")

# Creamos el modelo
model <- lm(y~age+sex+bmi+glu, data = input)
cat("# # # # MODELO # # # ","\n")
print(summary(model))

coeff.intercept <- coef(model)[1]
coeff.age <- coef(model)[2]
coeff.sex <- coef(model)[3]
coeff.bmi <- coef(model)[4]
coeff.glu <- coef(model)[5]


# Para realizar nuevas predicciones, creamos dataframe
age <- c(0.02, 0.05)
sex <- c(-0.044, 0.05)
bmi <- c(-0.044, 0.05)
glu <- c(-0.096, -0.046)
new_data <- data.frame(age, sex, bmi, glu)
resultado <- predict(model, new_data)
cat("# # # # PREDICCION # # # ","\n")
print(resultado)
