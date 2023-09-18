import pandas as pd

import utils.imports as imp
import utils.visuals as visu
import utils.processing as proc


data = imp.read_diabetes_txt("data/diabetes.tab.txt")
print("archivo txt cargado")

correlation_data = proc.get_correlations(data)

visual_object = visu.Visualizer(data)
# visual_object.save_correlations_heatmap()
# visual_object.save_histograms()
# visual_object.save_scatter_plots()
# visual_object.save_histogram_correlations()
# visual_object.save_correlations_heatmap()


normalized_data = proc.normalize_diabetes_data(data)
print("data normalized")

training, test = proc.split_data(normalized_data, 0.7)
training_input = pd.DataFrame(training, columns=["AGE", "BMI", "BP"])
training_output = pd.DataFrame(training, columns=["Y"])
test_input = pd.DataFrame(test, columns=["AGE", "BMI", "BP"])
test_output = pd.DataFrame(test, columns=["Y"])

model = proc.linear_regression(training_input, training_output)

test_predictions = proc.test_predictions(model, test_input)

coefficients = proc.get_coefficients(model)
print("Coefficients: ", coefficients)
MSE = proc.get_mean_squared_error(test_output,
                                  test_predictions)
print("Mean Squared Error: ", MSE)
R2 = proc.get_coefficient_determination(test_output,
                                        test_predictions)
print("R² Score: ", R2)

# Usemos columna SEX como variable categórica (logistic regression)
training, test = proc.split_data(normalized_data, 0.8)
training_input = pd.DataFrame(training, columns=["AGE", "BMI", "BP"])
training_output = pd.DataFrame(training, columns=["SEX"])
test_input = pd.DataFrame(test, columns=["AGE", "BMI", "BP"])
test_output = pd.DataFrame(test, columns=["SEX"])

training_output = proc.values_2_categorical(training_output)
test_output = proc.values_2_categorical(test_output)
model = proc.logistic_regression(training_input, training_output)
test_predictions = proc.test_predictions(model, test_input)

coefficients = proc.get_coefficients(model)
print("Logistic model Coefficients: ", coefficients)

names = ['male', 'female']
confusion_matrix = proc.get_confusion_matrix(test_output, test_predictions, names)
visu.save_confusion_matrix(confusion_matrix)
visu.save_roc_curve(test_output, test_predictions)
