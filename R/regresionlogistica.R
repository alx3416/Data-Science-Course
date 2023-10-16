# Ejemplo Regresión Logística

# dataset incluido en R "mtcars"
input <- mtcars[,c("am","cyl","hp","wt")]

# formula general y = 1/(1+e^-(a+b1x1+b2x2+b3x3+...))
model = glm(formula = am ~ cyl + hp + wt, data = input, family = binomial)

print(summary(model))

cyl <- c(4, 8)
hp <- c(80, 160)
wt <- c(2.2, 3.5)
new_data <- data.frame(cyl, hp, wt)
resultado <- predict(model, new_data, type = "response")
cat("# # # # PREDICCION # # # ","\n")
print(resultado)