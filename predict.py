import numpy as np

import joblib 



def predict_sales(input):
    d_predictor = joblib.load("saved/Sales_Predictor.pkl")

    predict = d_predictor.predict(input)
    return predict
