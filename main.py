import pandas as pd

import utils.imports as imp
import utils.visuals as visu
import utils.processing as proc


data = imp.read_diabetes_txt("data/diabetes.tab.txt")
print("archivo txt cargado")

correlation_data = proc.get_correlations(data)

visu.save_correlations_heatmap(data)

# visu.save_histograms(data)

# visu.save_scatter_plots(data, correlation_data)

# visu.save_histogram_correlations(data)

normalized_data = proc.normalize_diabetes_data(data)
print("data normalized")

training, test = proc.split_data(normalized_data, 0.7)
training_input = pd.DataFrame(training, columns=["AGE", "BMI", "BP"])
training_output = pd.DataFrame(training, columns=["Y"])
test_input = pd.DataFrame(test, columns=["AGE", "BMI", "BP"])
test_output = pd.DataFrame(test, columns=["Y"])

model = proc.simple_linear_regression(training_input, training_output)

test_predictions = proc.test_predictions(model, test_input)

coefficients = proc.get_coefficients(model)
print("Coefficients: ", coefficients)
MSE = proc.get_mean_squared_error(test_output,
                                  test_predictions)
print("Mean Squared Error: ", MSE)
R2 = proc.get_coefficient_determination(test_output,
                                        test_predictions)
print("R² Score: ", R2)

