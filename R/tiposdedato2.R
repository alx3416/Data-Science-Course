# Vector
#funcion c, combine
manzana <- c('rojo','verde',55)
print(manzana)

# lista
list1 <- list(c(2,5,3),21.3,sin)
print(list1)

# matriz
M = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = FALSE)
print(M)

# arreglo (array)
a <- array(c('green','yellow', 'red','blue'),dim = c(3,3,2))
print(a)

# Factores
apple_colors <- c('green','green','yellow','red','red','red','green')
factor_apple <- factor(apple_colors)
print(factor_apple)
print(nlevels(factor_apple))

# Data Frames
BMI <- 	data.frame(
  gender = c("Male", "Male","Female"), 
  height = c(152, 171.5, 165), 
  weight = c(81,93, 78),
  Age = c(42,38,26)
)
print(BMI)
