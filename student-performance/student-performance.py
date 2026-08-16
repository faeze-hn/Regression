import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_dirty.csv")

# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df[df.duplicated()])

df = df.drop_duplicates()
# print(df.shape)


df["Gender"] = df["Gender"].str.strip()
df["Gender"] = df["Gender"].str.lower()
df["City"] = df["City"].str.lower()
df["City"] = df["City"].replace("mashad", "mashhad")

# print(df["Gender"].unique())
# print(df["City"].unique())
# print(df["Age"].describe())
# print(df[["Math", "English", "Science"]].describe())
# print(df[(df["Age"] < 10) | (df["Age"] > 20)])
# print(df[(df["Math"] < 0) | (df["Math"] > 20)])
# print(df[(df["English"] < 0) | (df["English"] > 20)])
# print(df[(df["Science"] < 0) | (df["Science"] > 20)])

df.loc[(df["Age"] < 10) | (df["Age"] > 20), "Age"] = np.nan
df.loc[(df["Math"] < 0) | (df["Math"] > 20), "Math"] = np.nan
df.loc[(df["English"] < 0) | (df["English"] > 20), "English"] = np.nan
df.loc[(df["Science"] < 0) | (df["Science"] > 20),"Science"] = np.nan

# print(df[(df["Attendance"] <0 ) | (df["Attendance"] > 100 )])
# print(df[(df["Study_Hours"] > 24)])

df.loc[(df["Attendance"] <0 ) | (df["Attendance"] > 100 ), "Attendance"] = np.nan
df.loc[(df["Study_Hours"] > 24)] = np.nan

# print(df.isnull().sum())
# print(df.shape)
# print(df[df.isnull().any(axis=1)])
df = df.dropna(how="all")
# print(df.shape)
# print(df.isnull().sum())
# print(df["Age"].describe())
# print(df["Age"].median())
# print(df["Age"].mean())
df["Age"] = df["Age"].fillna(df["Age"].median())
# print(df["Age"].isnull().sum())

# print("Math")
# print(df["Math"].describe())
# print("Median:", df["Math"].median())

# print("\nEnglish")
# print(df["English"].describe())
# print("Median:", df["English"].median())

# print("\nScience")
# print(df["Science"].describe())
# print("Median:", df["Science"].median())

df["Math"] = df["Math"].fillna(df["Math"].median())

df["English"] = df["English"].fillna(df["English"].median())

df["Science"] = df["Science"].fillna(df["Science"].median())

# print(df["Attendance"].describe())
# print("Mean:", df["Attendance"].mean())
# print("Median:", df["Attendance"].median())
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].median()
)

Q1 = df["Study_Hours"].quantile(0.25)
Q3 = df["Study_Hours"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# print("Q1:", Q1)
# print("Q3:", Q3)
# print("IQR:", IQR)
# print("Lower:", lower_bound)
# print("Upper:", upper_bound)

# print(df[
#     (df["Study_Hours"] < lower_bound) |
#     (df["Study_Hours"] > upper_bound)
# ])

columns = ["Math", "English", "Science"]

for col in columns:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[
        (df[col] < lower) |
        (df[col] > upper)
    ]

    # print("\nColumn:", col)
    # print("Q1:", Q1)
    # print("Q3:", Q3)
    # print("IQR:", IQR)
    # print("Lower:", lower)
    # print("Upper:", upper)
    # print("Number of outliers:", len(outliers))

Q1 = df["Math"].quantile(0.25)
Q3 = df["Math"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# print(df[
#     (df["Math"] < lower) |
#     (df["Math"] > upper)
# ])

print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.info())
print(df.describe())
