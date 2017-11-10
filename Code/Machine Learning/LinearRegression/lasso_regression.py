from sklearn.linear_model import Lasso
from sklearn.datasets import load_iris
import numpy as np
from sklearn.model_selection import train_test_split


iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
	iris_dataset['data'], iris_dataset['target'], random_state=0
	)

lr = Lasso().fit(X_train, y_train)

print ("Training set score: {:.5f}".format(lr.score(X_train, y_train)))
print ("Testing set score: {:.5f}".format(lr.score(X_test, y_test)))
print ("Number of Features: {}".format(np.sum(lr.coef_ != 0)))