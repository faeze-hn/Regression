import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv("FuelConsumption.csv")

cdf = df[[
    "ENGINESIZE",
    "CO2EMISSIONS"]]

# plt.scatter(
#     cdf.ENGINESIZE,
#     cdf.CO2EMISSIONS,
# )
# plt.xlabel("ENGINESIZE")
# plt.ylabel("CO2MISSIONS")
# plt.show()

msk = np.random.rand(len(df)) < 0.8

train = cdf[msk]
test = cdf[~msk]

regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[["ENGINESIZE"]])
train_y = np.asanyarray(train[["CO2EMISSIONS"]])

regr.fit(train_x,train_y)

print("Coefficient: ",regr.coef_)
print("Intercept: ", regr.intercept_)

plt.scatter(
    train.ENGINESIZE,
    train.CO2EMISSIONS,
    color = "blue"
)

plt.plot(train_x,
         regr.coef_[0][0]*train_x + regr.intercept_[0],
         "-r")

plt.show()

test_x = np.asanyarray(test[["ENGINESIZE"]])
test_y = np.asanyarray(test[["CO2EMISSIONS"]])

test_y_ = regr.predict(test_x)

MAE = np.mean(np.absolute(test_y_ - test_y))
MSE = np.mean((test_y_ - test_y) **2)
r2 = r2_score(test_y, test_y_)
print(r2)