# This implementation uses Numpy's inbuilt kNN Classifier.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris_dataset = load_iris() # Loading an inbuilt dataset

# Split iris_dataset into Training and Testing Dataset
X_train, X_test, y_train, y_test = train_test_split(
	iris_dataset['data'], iris_dataset['target'], random_state=0
	)

# Creating an Object of the KNeighborsClassifier
myKNN = KNeighborsClassifier(n_neighbors = 20) # n_neighbors is the parameter which decides how many neighbors are to be considered

# Fit Classifier with training data
myKNN.fit(X_train, y_train)

# Let Classifier make prediction 

prediction = myKNN.predict(X_test)
print ("Prediction: {}".format(prediction))
print ("Predicted Target Name: {}".format(iris_dataset['target_names'][prediction]))



