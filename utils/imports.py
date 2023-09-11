import pandas as pd


def read_diabetes_txt(path):
    datos = pd.read_csv(path, sep='\t')
    return datos