import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# x =range(5)

# plt.plot(x, [x1 for x1 in x], label = "Linear")
# plt.plot(x, [x1*x1 for x1 in x], label = "square")
# plt.plot(x, [x1 * x1 * x1 for x1 in x], label = "triple")

# plt.legend()
# plt.grid(True)
# # plt.axis([-1,5,-1,10])
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("learning matplotlib")
# plt.savefig('plot.png')
# plt.show()

# dict = {"A" : 25 , "B" : 70 , "C" : 90}

# for i, key in enumerate(dict):
#     plt.bar(i,dict[key])

# plt.show()

# plt.figure(figsize=(3,3))
# plt.pie([40,20,5], labels=['bikes', 'cars', 'buses'])
# plt.show()

# students = pd.DataFrame({
#     "Name": ["Ali", "Sara", "Reza", "Mina", "Amir", "Neda"],
#     "Math": [18, 15, 20, 17, 16, 19],
#     "Python": [19, 18, 17, 20, 15, 18],
#     "Physics": [17, 19, 18, 16, 20, 17]
# })

# students["Average"] = (
#     students["Math"] +
#     students["Python"] +
#     students["Physics"]
# ) / 3

# LINE PLOT

# plt.plot(students["Name"],students["Math"])
# plt.title("Math Scores")
# plt.xlabel("Students")
# plt.ylabel("Score")
# plt.show()

# BAR CHART

# plt.bar(students["Name"],students["Python"])
# plt.title("Python Scores")
# plt.xlabel("Students")
# plt.ylabel("Python Score")
# plt.show()

# PIE CHART

# plt.figure(figsize=(4,4))
# plt.pie(students["Physics"], labels=students["Name"], autopct="%1.1f%%")
# plt.title("Physics Scores")
# plt.show()

# SCATTER PLOT

# x = students["Math"]
# y = students["Python"]
# plt.scatter(x,y)
# plt.title("Math VS Python")
# plt.xlabel("Math")
# plt.ylabel("Python")
# plt.show()

# HISTOGRAM

# plt.hist(students["Average"], bins=5)
# plt.title("Average Score")
# plt.xlabel("Average")
# plt.ylabel("Frequency")
# plt.show()

# plt.figure(figsize=(8, 5))

# plt.plot(
#     students["Math"],
#     color="red",
#     linestyle="--",
#     marker="o"
# )

# plt.title("Math Scores")
# plt.xlabel("Students")
# plt.ylabel("Score")
# plt.grid(True)

# plt.show()

# plt.plot(students["Math"], label = "Math",color = "red")
# plt.plot(students["Python"], label = "Python", color = "blue")
# plt.plot(students["Physics"], label = "Physics", color = "green")
# plt.legend()
# plt.grid(True)
# plt.title("Students Scores Comparison")
# plt.show()

# shop = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "SSD"],
#     "Sales": [250000, 20000, 22500, 96000, 80000]
# })

# plt.figure(figsize=(12,5))
# plt.subplot(1,2,1)
# plt.bar(shop["Product"], shop["Sales"])
# plt.title("Store Sales")
# plt.xlabel("Product")
# plt.ylabel("Sales")

# plt.subplot(1,2,2)
# max_index = shop["Sales"] . idxmax()
# explode = [0,0,0,0,0]
# explode[max_index] = 0.1
# plt.pie(shop["Sales"],labels= shop["Product"], autopct="%1.1f%%", explode= explode)


# plt.title("Store Sales Distribution")
# plt.show()

scores = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75,
          78, 80, 82, 85, 90, 92, 95]

plt.hist(scores)
plt.title("Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()