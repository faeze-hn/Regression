import pandas as pd
import numpy as np

# arr = numpy.array([10,20,30,40,50])
# series = pandas.Series(arr)

# print(series[2:4])

# listx = [10,20,30,40]
# table = pandas.DataFrame(listx)

# print(table)

# data = [{'a':1, 'b':2}, {'a':2, 'b':4, 'c':18}]
# table = pandas.DataFrame(data, index=["first","second"])

# print(table)

# data = {'one':pandas.Series([1,2,3],index = ["a","b","c"]),
#         'two':pandas.Series([1,2,3,4],index = ["a","b","c","d"])}

# table= pandas.DataFrame(data)

# print(table)

# grades = pandas.Series([18,15,20,17,19])

# print(grades[2])
# print(grades[3:])
# print(grades.mean())
# print(grades.max())
# print(grades.min())
# print(grades[grades>17])
# print(grades+2)
# print(grades)

# students = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Reza", "Mina", "Amir"],
#     "Age": [20, 22, 21, 20, 23],
#     "Math": [18, 15, 20, 17, 16],
#     "Python": [19, 18, 17, 20, 15]
# })

# print(students)
# print(students[:5])
# print(students.tail(5))
# print(students.columns)
# print(students.shape)
# print(students["Math"].dtype)
# print(students.info())
# print(students["Name"])
# print(students.loc[:,["Name","Python"]])
# print(students.iloc[0])
# print(students.iloc[[2]])
# print(students.iloc[1:4])
# print(students["Math"].mean())
# print(students["Python"].mean())
# print(students["Python"].max())
# print(students["Age"].min())
# print(students["Math"].sum())

# students["Average"] = (students["Math"] + students["Python"]) / 2

# print(students)
# print(students[students["Math"]>17])
# print(students[students["Age"]>20])
# print(students[(students["Math"]>16) & (students["Python"]>17)])

# print(students.sort_values("Age", ascending=True))

# students["Math"] += 2
# students.loc[students["Python" ]< 18 , "Python"] += 5
# print(students)

# print(students[students["Average"]> 18])
# print(students)

# shop = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "SSD"],
#     "Price": [50000, 800, 1500, 12000, 4000],
#     "Quantity": [5, 25, 15, 8, 20]
# })

# shop["Total"] = (shop["Price"] * shop["Quantity"])

# print(shop["Total"].sum())
# print(shop["Price"].max())
# print(shop.loc[shop["Price"].idxmax(), "Product"])
# print(shop.loc[shop["Quantity"].idxmax(), "Product"])
# print(shop[shop["Price"]>5000])

# shop = shop.sort_values("Total",ascending=False)
# print(shop)

# shop["Status"] = np.where(shop["Quantity"]<10, "Low", "ok")
# print(shop)

students = pd.DataFrame({
    "Name": ["Ali", "Sara", "Reza", "Mina", "Amir", "Neda"],
    "Age": [20, 22, 21, 20, 23, 19],
    "Math": [18, 15, 20, 17, 16, 19],
    "Python": [19, 18, 17, 20, 15, 18],
    "Physics": [17, 19, 18, 16, 20, 17]
})

# print(students)
# print(students.head(3))
# print(students.tail(2))
# print(students.columns)
# print(students.shape)
# print(students.dtypes)
# students.info()

# print(students["Name"])
# print(students[["Name","Math"]])
# print(students.iloc[0])
# print(students.iloc[-1])
# print(students.iloc[1:5])
# print(students.loc["Physics"])
# print()

# print(students["Math"].mean())
# print(students["Python"].max())
# print(students["Age"].min())
# print(students["Physics"].sum())
# print(students["Age"].mean())
# print((students["Math"] + students["Python"]).sum())

# print(students[students["Math"] > 17])
# print(students[students["Age"] < 21])
# print(students[students["Python"] < 18])
# print(students[(students["Math"] > 16 ) & (students["Physics"] > 17)])
# print(students.loc[students["Python"] >= 18, "Name"])

students["Average"] = (students["Math"] + students["Python"] + students["Physics"]) / 3

students["Total"] = (students["Math"] + students["Python"] + students["Physics"])

students["Status"] = np.where(students["Average"] >= 18 , "Excellent", "Normal")

# print(students.sort_values("Math", ascending=False))
# print(students.sort_values("Age", ascending=True))
# print(students.sort_values("Average", ascending=False))

# print(students.loc[students["Average"].idxmax()])
# print(students.loc[students["Average"].idxmax(), "Name"])
# print(students.loc[students["Average"].idxmin()])
# print(len(students.loc[students["Average"] > 18]))
# print(students["Average"].mean())

# print(students["Math"] + 2)
# print(np.where(students["Python"] < 18 , students["Python"] + 5 , students["Python"]))