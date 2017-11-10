# Performance of kNN Classifier using different number of neighbors.
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

cancer_dataset = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer_dataset.data, cancer_dataset.target, stratify=cancer_dataset.target, random_state=66)

training_accuracy = []
test_accuracy = []

neighbors_setting = range(1, 20)

for n_neighbors in neighbors_setting:
	Classifier = KNeighborsClassifier(n_neighbors=n_neighbors)
	Classifier.fit(X_train, y_train)

	training_accuracy.append(Classifier.score(X_train, y_train))
	test_accuracy.append(Classifier.score(X_test, y_test))


plt.plot(neighbors_setting, training_accuracy, label="Training Accuracy")
plt.plot(neighbors_setting, test_accuracy, label="Testing Accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Number of Neighbors")
plt.show()
