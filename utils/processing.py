import os
import math as mt
import pandas as pd


def check_output_folder(path):
    if os.path.isdir(path):
        pass
    else:
        os.makedirs(path)
        print(path+" folder created")


def save_correlations(data):
    check_output_folder("output")
    data.to_csv("output/correlations.csv")


def get_correlations(data):
    correlations_data = data.corr()
    save_correlations(correlations_data)
    return correlations_data


def normalize_diabetes_data(data):
    mu_data = data.mean()
    std_data = data.std()
    x = data.sub(mu_data, axis='columns')
    x2 = x.div(std_data, axis='columns')
    val = (1 / mt.sqrt(442))
    x3 = x2.mul(val, axis='columns')
    x3["Y"] = data["Y"]
    return x3

