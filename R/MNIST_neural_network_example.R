library(dslabs)
mnist <- read_mnist(download = TRUE)

mnist[["train"]][["images"]] = mnist[["train"]][["images"]]/255
mnist[["test"]][["images"]] = mnist[["test"]][["images"]]/255

# mnist[["train"]][["labels"]] = factor(mnist[["train"]][["labels"]])
# mnist[["test"]][["labels"]] = factor(mnist[["test"]][["labels"]])

model <- mlp(mnist[["train"]][["images"]], mnist[["train"]][["labels"]], 
             maxit=5, size = c(16), inputsTest=mnist[["test"]][["images"]], 
             targetsTest=mnist[["test"]][["labels"]])

predictions <- predict(model,mnist[["test"]][["images"]])
confusionMatrix(mnist[["test"]][["labels"]],predictions)