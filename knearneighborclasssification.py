import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

df = pd.read_csv("teleCust1000t.csv")

# print(df["custcat"].value_counts())

df["income"].hist(bins=50, edgecolor="black")
# plt.title("Income of customers")
# plt.xlabel('income')
# plt.ylabel("frequency")
# plt.grid(True, alpha=0.3)
# plt.show()

# print(df.columns)

X = df.drop("custcat", axis =1).values
y = df["custcat"].values
# print(y[0:5])

scaler = StandardScaler()
X = scaler.fit_transform(X.astype(float))

# print(X[0:5])
# print("mean: ", X.mean(axis=0).round(2))
# print("std: ", X.std(axis=0).round(2))

X_train, X_test, y_train, y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state= 4
)

# print('Train set:', X_train.shape, y_train.shape)
# print('Test set:', X_test.shape, y_test.shape)

k=4
neigh = KNeighborsClassifier(n_neighbors=k).fit(X_train,y_train)

yhat = neigh.predict(X_test)
# print(yhat[0:5])

# print("Train set accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
# print("Test set accuracy: ", metrics.accuracy_score(y_test,yhat))

ks = 10
mean_acc = np.zeros(ks-1)
std_acc = np.zeros(ks-1)

for n in range(1, ks):
    neigh = KNeighborsClassifier(n_neighbors=n).fit(X_train,y_train)
    yhat = neigh.predict(X_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test, yhat)
    std_acc[n-1] = np.std( yhat == y_test ) / np.sqrt(yhat.shape[0])


# print(mean_acc)

plt.plot(range(1, ks), mean_acc, 'g')
plt.fill_between(range(1, ks), mean_acc - 1 * std_acc, mean_acc + 1 * std_acc, alpha=0.10)
plt.fill_between(range(1, ks), mean_acc - 3 * std_acc, mean_acc + 3 * std_acc, alpha=0.10, color="green")
plt.legend(('Accuracy ', '+/- 1xstd', '+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Neighbors (K)')
plt.tight_layout()
plt.show()

print("The best accuracy was with", mean_acc.max(), "with k=", mean_acc.argmax()+1)