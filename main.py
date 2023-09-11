import utils.imports as imp
import utils.visuals as visu
import utils.processing as proc


data = imp.read_diabetes_txt("data/diabetes.tab.txt")
print("archivo txt cargado")

correlation_data = proc.get_correlations(data)
visu.save_histograms(data)

visu.save_scatter_plots(data, correlation_data)

visu.save_histogram_correlations(data)
