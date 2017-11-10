from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
	iris_dataset['data'], iris_dataset['target'], random_state=0
	)

myKNN = KNeighborsRegressor(n_neighbors=3)

myKNN.fit(X_train, y_train)

print ("Test Set Prediction:\n{}\n".format(myKNN.score(X_test, y_test)))