import utils.imports as imp
import utils.visuals as visu
import utils.processing as proc
import pandas as pd

data = imp.read_natalidad_dataset_2022("data\conjunto_de_datos_natalidad_2022_csv\conjunto_de_datos\conjunto_de_datos_natalidad_2022.csv")
print("archivo txt cargado")

data_edades_padres = data[["ent_ocurr", "edad_madn", "edad_padn", "hora_nac"]]
# quitar datos donde edad >=99
# idx_filtered = data_edades_padres[data_edades_padres["ent_ocurr"] != 22].index
# data_edades_padres.drop(idx_filtered, inplace=True)
idx_filtered = data_edades_padres[data_edades_padres["edad_madn"] == 99].index
data_edades_padres.drop(idx_filtered, inplace=True)
idx_filtered = data_edades_padres[data_edades_padres["edad_padn"] == 99].index
data_edades_padres.drop(idx_filtered, inplace=True)
idx_filtered = data_edades_padres[data_edades_padres["hora_nac"] == 99].index
data_edades_padres.drop(idx_filtered, inplace=True)

# visu.save_2d_histogram_edades(data_edades_padres)
visu.save_heatmap_edades_logaritmico(data_edades_padres)
# Implementar plotly 2d histogram
print("grafica de padres completa Queretaro")
visu.save_grafica_polar(data_edades_padres)
