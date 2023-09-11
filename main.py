import utils.imports as imp
import utils.visuals as visu
import utils.processing as proc


data = imp.read_diabetes_txt("data/diabetes.tab.txt")
print("archivo txt cargado")

correlation_data = proc.get_correlations(data)
# visu.save_histograms(data)

# visu.save_scatter_plots(data, correlation_data)

# visu.save_histogram_correlations(data)

data_normalized = proc.normalize_diabetes_data(data)
print("data normalized")

# Z = 1/sqrt(n) * ((x-mu)/sigma)
# data.mean()
# x = data["AGE"]
# x = data.loc[:, "AGE"]
# x.mean()

input_data = data_normalized["BMI"]
output_data = data_normalized["Y"]
training_input, test_input = proc.split_data(input_data)
training_output, test_output = proc.split_data(output_data)

model = proc.simple_linear_regression(training_input, training_output)

test_predictions = proc.test_predictions(model, test_input)

print(proc.get_coefficients(model))

