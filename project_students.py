import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

students = pd.read_csv("students.csv")

# students.head(5)
# students.tail(5)
# students.info()
# students.describe()
# print(students)

students["Age"] = students["Age"].fillna(
    students["Age"].mean()
)
students["Math"] = students["Math"].fillna(
    students["Math"].mean()
)
students["Physics"] = students["Physics"].fillna(
    students["Physics"].mean()
)
students["English"] = students["English"].fillna(
    students["English"].mean()
)

# print(students.isnull().sum())
students["Average"] = (students["Math"] + students["English"] + students["Physics"]) / 3
students["Status"] = "Fail"
students.loc[
    students["Average"] >= 17,
    "Status"
] = "Pass"

def grade(score):
    if score >= 19:
        return "A"
    elif score >= 17:
        return "B"
    elif score >= 15 :
        return "C"
    else :
        return "D"

students ["Grade"] = students["Average"] .apply(grade)
# print(students[students["Average"] > 18])
# print(students[students["Department"] == "Computer"])
# print(students[students["Math"].between(17,20)])
# print(students[students["Department"].isin(["Computer", "Electrical"])])
students = students.sort_values("Average",ascending=False)

# print(students.nlargest(3,"Average"))
print(students.groupby("Department")["Average"].mean())
print(students.groupby("Department")["Average"].max())
print(students.groupby("Department")["Average"].count())
print(students.groupby("Department")["Average"].agg(
    ["mean","max","min","count"]
))

# avg_department = students.groupby("Department")["Average"].mean()
# avg_department.plot(kind="bar")
# plt.title("Average Score by Department")
# plt.xlabel("Department")
# plt.ylabel("Average")
# plt.show()

# cnt_department = students.groupby("Department")["Name"].count()
# cnt_department.plot(
#     kind="pie",
#     autopct = "%1.1f%%"      
#       )
# plt.title("Number of Students")
# plt.ylabel("")
# plt.show()

# students["Average"].plot(kind="hist")
# plt.title("Average Distribution")
# plt.xlabel("Average")
# plt.ylabel("Students")
# plt.show()

# students.plot(
#     kind = "scatter",
#     x = "Math",
#     y = "Physics"
# )
# plt.title("Math vs Physics")
# plt.xlabel("Math Score")
# plt.ylabel("Physics Score")

# plt.show()

students.plot(
    kind = "line",
    x= "Name",
    y = "Average"
    )
plt.title("Students Average Scores")
plt.xlabel("Student Name")
plt.ylabel("Average")

plt.show()

students.to_csv("students_result.csv", index=False)