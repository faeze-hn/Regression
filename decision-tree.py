import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import tree

df = pd.read_csv("drug200.csv")

x = df.drop("Drug", axis = 1).values

le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
x[:, 1] = le_sex.transform(x[:,1])

le_BP = preprocessing.LabelEncoder()
le_BP.fit(["LOW", "NORMAL", "HIGH"])
x[:, 2]= le_BP.transform(x[:,2])

le_chol = preprocessing.LabelEncoder()
le_chol.fit(["NORMAL", "HIGH"])
x[:, 3] = le_chol.transform(x[:,3])

y = df["Drug"]

x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.3, random_state=3
)

drugtree = DecisionTreeClassifier(criterion="entropy", max_depth=4)
drugtree.fit(x_train,y_train)
predtree= drugtree.predict(x_test)

print("DecisionTree's Accuracy: ", metrics.accuracy_score(y_test,predtree))

plt.figure(figsize=(15, 10))
tree.plot_tree(drugtree, 
               feature_names=['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K'],
               class_names=drugtree.classes_,
               filled=True,
               rounded=True)
plt.show()