from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset.data, iris_dataset.target, stratify=iris_dataset.target, random_state=66)

training_accuracy = []
test_accuracy = []

neighbor_settings = range(1, 20)

for n_neighbors in neighbor_settings:

	Regressor = KNeighborsRegressor(n_neighbors=n_neighbors)
	Regressor.fit(X_train, y_train)

	training_accuracy.append(Regressor.score(X_train, y_train))
	test_accuracy.append(Regressor.score(X_test, y_test))

plt.plot(neighbor_settings, training_accuracy, label="Training Accuracy")
plt.plot(neighbor_settings, test_accuracy, label="Testing Accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Number of Neighbors")
plt.show()
