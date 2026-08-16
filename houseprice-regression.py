import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

df = pd.read_csv("housePrice.csv")



df["Area"] = pd.to_numeric(
    df["Area"].astype(str).str.replace(",",""),
    errors="coerce"
)

df = df.dropna(subset=["Address", "Area"])
df = df[df["Area"]<=1000]

# print(df.shape)
# print(df.info())
# print(df.isnull().sum())
# print(df["Area"].describe())

# print(df.head())
# print(df.describe())
# print(df["Room"].value_counts())

# plt.scatter(df["Area"], df["Price"])
# plt.xlabel("Area")
# plt.ylabel("Price")
# plt.title("Area VS Price")
# plt.show()

# print(df.nlargest(10,"Area")[["Area", "Room", "Address", "Price"]])
# print(df.nlargest(10, "Price")[["Area", "Room", "Address", "Price"]])

df["Price_per_Area"] = df["Price"] / df["Area"]

# print(
#     df.nlargest(10,"Price_per_Area")[["Area", "Room", "Address", "Price", "Price_per_Area"]]
# )
df = df.drop(columns=["Price_per_Area"])

x = df.drop(columns = ["Price", "Price(USD)"])
y = df["Price"]

# print(x.head())
# print(y.head())

# print(x.shape)
# print(y.shape)

df["Parking"] = df["Parking"].astype(int)
df["Warehouse"] = df["Warehouse"].astype(int)
df["Elevator"] = df["Elevator"].astype(int)

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

# print("Train: ", x_train.shape)
# print("Test: ", x_test.shape)
# print("Train: ", y_train.shape)
# print("Test: ",y_test.shape)

categorical_features = ["Address"]

preprocessor = ColumnTransformer(
    transformers = [
        ("address",OneHotEncoder(handle_unknown="ignore"),categorical_features)
    ],
    remainder="passthrough"
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test,y_pred)

# print("MAE: ", mae)
# print("MSE: ", mse)
# print("RMSE: ", rmse)
# print("R2: ", r2)

comparison = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

comparison["Error"] = comparison["Actual"] - comparison["Predicted"]

print(comparison.head(10))