import seaborn as sns
import matplotlib.pyplot as plt
import utils.processing as proc
from sklearn import metrics


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
