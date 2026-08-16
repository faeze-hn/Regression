import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("housePrice.csv")

# print(df.shape)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.isnull().sum())
# print(df['Area'].unique()[-20:])   # آخر لیست unique رو ببین

df["Area"] = pd.to_numeric(
    df["Area"].astype(str).str.replace(",",""),
    errors="coerce"
)
# print(df['Area'].isnull().sum())      
# print(df['Area'].describe())          
# print(df[df['Area'] > 400][['Area', 'Address', 'Price']].sort_values('Area', ascending=False).head(15))

df = df[df["Area"] <= 500]
df = df.dropna(subset=["Address"])
# print("rows: ", len(df))
# print(df['Area'].describe())
# print(df.isnull().sum())

df["Parking"] = df["Parking"].astype(int)
df["Warehouse"] = df["Warehouse"].astype(int)
df["Elevator"] = df["Elevator"].astype(int)

# print(df[['Parking', 'Warehouse', 'Elevator']].head(10))
# print(df[['Parking', 'Warehouse', 'Elevator']].dtypes)

le = LabelEncoder()
df["Address_Encoded"] = le.fit_transform(df["Address"])

# print(df[['Address', 'Address_Encoded']].head(15))
# print("unique address: ", df['Address'].nunique())

x = df[["Area", "Room", "Parking", "Warehouse", "Elevator", "Address_Encoded"]]
y = df[["Price(USD)"]]

# print(x.head())
# print(y.head())

X_train, X_test, Y_train, Y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=42
)

# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)
# print("y_train shape:", Y_train.shape)
# print("y_test shape:", Y_test.shape)
model = LinearRegression()
model.fit(X_train,Y_train)

y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(Y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(Y_test, y_pred)))
print("R2 Score:", r2_score(Y_test, y_pred))