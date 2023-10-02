import seaborn as sns
import matplotlib.pyplot as plt
import utils.processing as proc
from sklearn import metrics
import plotly.graph_objects as go
import plotly.express as px


def save_confusion_matrix(confusion):
    proc.check_output_folder("output")
    new_fig = plt.figure()
    sns.heatmap(confusion, annot=True, cmap='Blues')
    plt.savefig("output/confusion_matrix.png")
    plt.close(new_fig)


def save_roc_curve(diabetes_y_test, diabetes_y_pred):
    proc.check_output_folder("output")
    new_fig = plt.figure()
    metrics.RocCurveDisplay.from_predictions(diabetes_y_test, diabetes_y_pred)
    plt.savefig("output/curve_ROC.png")
    plt.close(new_fig)


def save_histogram_edades_padres(data):
    proc.check_output_folder("output")
    fig = sns.displot(data, kde=True)
    fig.savefig("output/hsitograma_edades_padres.png")
    plt.close()


def save_2d_histogram_edades(data):
    proc.check_output_folder("output")
    fig = go.Figure(go.Histogram2d(x=data["edad_padn"], y=data["edad_madn"]))
    fig.show()
    fig.write_image("output/histograma_2d_edades_padres.svg")


def save_heatmap_edades(data):
    proc.check_output_folder("output")
    fig = go.Figure(px.density_heatmap(data, x="edad_padn", y="edad_madn",
                                       color_continuous_scale="Rainbow",
                                       range_color=[0, 100],
                                       title="Edades padres recien nacidos México 2022"))
    fig.show()
    fig.write_image("output/heatmap_edades_padres.svg")


def save_grafica_polar(data):
    proc.check_output_folder("output")
    freqs = data["hora_nac"].value_counts()
    freqs = freqs.sort_index()
    theta_values = freqs.index
    theta_values = theta_values.astype(str)
    trace = go.Scatterpolar(r=freqs.values, theta=theta_values,
                            fill='toself')
    polar_data = trace
    figure = go.Figure(data=polar_data, layout=None)
    figure.update_polars(radialaxis=dict(visible=False))
    figure.write_image("output/polar_hora_nacimiento.svg")
    figure.show()


class Visualizer:
    def __init__(self, data):
        self.data = data
        print("class constructed or initialized")

    def save_histogram(self, column):
        proc.check_output_folder("output/histograms")
        fig = sns.displot(self.data[column], kde=True)
        fig.savefig("output/histograms/histogram_" + column + ".png")
        plt.close()

    def save_histograms(self):
        for col in self.data.columns:
            self.save_histogram(col)

    def save_scatter_plot(self, var1, var2, corr_value):
        proc.check_output_folder("output/scatterplots")
        new_fig = plt.figure()
        sns.scatterplot(data=self.data, x=var1, y=var2).set(title=var1 + " vs " + var2 + " r = " + corr_value)
        plt.savefig("output/scatterplots/scatter_" + var1 + "_" + var2 + ".png")
        plt.close(new_fig)

    def save_scatter_plots(self):
        columns_pending = self.data.columns
        for var1 in self.data.columns:
            columns_pending = columns_pending.drop(var1)
            for var2 in columns_pending:
                if not var1 == var2:
                    corr_value = str(self.data.corr().loc[var1][var2])
                    self.save_scatter_plot(var1, var2, corr_value)
                else:
                    continue

    def save_histogram_correlations(self):
        proc.check_output_folder("output")
        fig = sns.pairplot(self.data, hue="SEX")
        fig.savefig("output/All_histograms.png")
        plt.close()

    def save_correlations_heatmap(self):
        proc.check_output_folder("output")
        new_fig = plt.figure()
        sns.heatmap(self.data.corr(), annot=True, fmt='.2f').set(title="Correlations for Diabetes Dataset")
        plt.savefig("output/correlations_heatmap.png")
        plt.close(new_fig)
