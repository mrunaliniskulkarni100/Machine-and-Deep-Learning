from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


boston = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, stratify=boston.target, random_state=42)


LogReg = LogisticRegression().fit(X_train, y_train)
print ("Training Set Score for C = 1 : {:.5f}".format(LogReg.score(X_train, y_train)))
print ("Testing Set Score for C = 1 : {:.5f}\n".format(LogReg.score(X_test, y_test)))


LogReg01 = LogisticRegression(C=0.01).fit(X_train, y_train) # Default value of c is 1
print ("Training Set Score for C = 0.01 : {:.5f}".format(LogReg01.score(X_train, y_train)))
print ("Testing Set Score for C = 0.01 : {:.5f}\n".format(LogReg01.score(X_test, y_test)))


LogReg100 = LogisticRegression(C=100).fit(X_train, y_train) # Default value of c is 1
print ("Training Set Score for C = 100 : {:.5f}".format(LogReg100.score(X_train, y_train)))
print ("Testing Set Score for C = 100 : {:.5f}\n".format(LogReg100.score(X_test, y_test)))


# Plotting data using Matplotlib
plt.plot(LogReg.coef_.T, 'o', label="C=1")
plt.plot(LogReg01.coef_.T, '^', label="C=0.01")
plt.plot(LogReg100.coef_.T, 'v', label="C=100")


plt.show()