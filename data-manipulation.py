import pandas as pd
import numpy as np

# students = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Reza", "Neda", "Mina"],
#     "Age": [20, 22, 19, 21, 20],
#     "Math": [18, 15, 20, 17, 19],
#     "Physics": [17, 18, 19, 16, 20]
# })

# print(students[students["Name"].isin(["Ali", "Sara"])])
# print(students[students["Math"].between(17,20)])
# print(students.query("Age > 19 and Physics > 18"))
# def grade(score):
#     if score >=18 :
#         return "A"
#     elif score >= 15:
#         return "B"
#     else:
#         return "C"


# students["Average"] = (students["Math"] + students["Physics"]) / 2
# students["Grade"] = students["Average"].apply(grade)
# students["Bonus"] = students["Math"] + 2
# students.drop("Bonus", axis=1, inplace=True)
# students.rename(
#     columns={
#         "Physics" : "Physics Score"
#     },
#     inplace=True
# )

# students ["Total"] = students["Math"] + students["Physics"]
# students["Pass"] = "No"
# students.loc[students["Math"] >= 10, "Pass"] = "Yes"
# def level(lv) :
#     if lv >= 18 :
#         return "Excellent"
#     elif lv >=15 :
#         return "Good"
#     else:
#         return "weak"
# students["Math"] = students["Math"].apply(level)
# students.rename(
#     columns={"Physics":"Physics_Score"},
#     inplace=True
# )
# print(students)

# HANDLING MISSING DATA

# students = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Reza", "Neda", "Mina"],
#     "Age": [20, np.nan, 19, 21, np.nan],
#     "Math": [18, 15, np.nan, 17, 19]
# })

# print(students.isnull().sum())
# print(students.dropna())
# print(students.fillna(100))
# print(students.fillna(students["Age"].mean()))

# GROUPBY

# students = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Reza", "Neda", "Mina", "Amir"],
#     "Department": [
#         "Computer",
#         "Computer",
#         "Electrical",
#         "Computer",
#         "Electrical",
#         "Electrical"
#     ],
#     "Math": [18, 15, 20, 17, 19, 16]
# })

# print(students.groupby("Department")["Math"].mean())
# print(students.groupby("Department")["Math"].sum())
# print(students.groupby("Department")["Math"].max())
# print(students.groupby("Department")["Math"].count())
# print(students.groupby("Department")["Math"].agg(
#     ["mean","max","min","sum", "count"]
# ))

# MERGE

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Ali", "Sara", "Reza"]
})

scores = pd.DataFrame({
    "ID": [1, 3, 4],
    "Math": [18, 20, 17]
})

new_dataFrame = pd.merge(students,scores,on="ID", how="inner")
new_dataFrame1 = pd.merge(students,scores,on="ID", how="left")
new_dataFrame2 = pd.merge(students,scores,on="ID", how="right")
new_dataFrame3 = pd.merge(students,scores,on="ID", how="outer")