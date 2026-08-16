import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl
from sklearn import linear_model

df = pd.read_csv("FuelConsumption.csv")

cdf = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_CITY", "FUELCONSUMPTION_HWY", "FUELCONSUMPTION_COMB", "CO2EMISSIONS"]]

msk = np.random.rand(len(df)) < 0.8 
train = cdf[msk]
test = cdf[~msk]

regr = linear_model.LinearRegression()
x = np.asanyarray(train[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]])
y = np.asanyarray(train[["CO2EMISSIONS"]])

regr.fit(x,y)

# the coefficient
print("Coefficents: ", regr.coef_)
print("Intercept: ", regr.intercept_)

y_hat = regr.predict(test[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]])
x = np.asanyarray(test[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]])
y = np.asanyarray(test[["CO2EMISSIONS"]])
print("Residual sum of square: " , np.mean((y_hat - y)**2))
print("Variance score: ", regr.score(x,y))