import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import jaccard_score, classification_report, log_loss, confusion_matrix
import seaborn as sns


churndf = pd.read_csv("ChurnData.csv")

churndf = churndf[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip', 'callcard', 'wireless','churn']]
churndf["churn"] = churndf['churn'].astype(int)

x = churndf[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip']]
y = churndf['churn']

scaler = preprocessing.StandardScaler()
x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size = 0.2, random_state=4
    )

LR = LogisticRegression(C=0.01, solver= 'liblinear').fit(x_train,y_train)

yhat = LR.predict(x_test)
yhat_prob = LR.predict_proba(x_test)

print(jaccard_score(y_test,yhat,pos_label=0))
print(classification_report(y_test, yhat))
print(log_loss(y_test, yhat_prob))


cm = confusion_matrix(y_test, yhat, labels=[1,0])

plt.figure(figsize=(6,4))
sns.heatmap(cm,annot=True, fmt='d', cmap='Blues',
            xticklabels=['churn=1', 'churn=0'],
            yticklabels=['churn=1', 'churn=0'])

plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Confusion Matrix')
plt.show()
