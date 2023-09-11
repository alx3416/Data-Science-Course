import os
import math as mt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


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


def use_only_one_feature(data):
    diabetes_one = data[:, np.newaxis, 2]
    return diabetes_one


def split_data(data):
    training_data = data[:-20]
    test_data = data[-20:]
    return training_data, test_data


def simple_linear_regression(input_train, output_train):
    regr = linear_model.LinearRegression()
    inputs = input_train.values.reshape(-1, 1)
    regr.fit(inputs, output_train)
    return regr


def test_predictions(model, input_test):
    output_test = model.predict(input_test.values.reshape(-1, 1))
    return output_test


def get_coefficients(model):
    return model.coef_


def get_mean_squared_error(output_test, output_predicted):
    return mean_squared_error(output_test, output_predicted)


def get_coefficient_determination(output_test, output_predicted):
    return r2_score(output_test, output_predicted)
