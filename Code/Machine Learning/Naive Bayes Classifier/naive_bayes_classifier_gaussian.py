import numpy as np

X=np.array([[-1, 1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y=np.array([1, 1, 1, 2, 2, 2])

from sklearn.naive_bayes import GaussianNB

Classifier=GaussianNB()
Classifier.fit(X, Y)

print(Classifier.predict([[-0.8, -1]]))

Classifier=GaussianNB()
Classifier.partial_fit(X, Y, np.unique(Y))

print(Classifier.predict([[-0.8, -1]]))