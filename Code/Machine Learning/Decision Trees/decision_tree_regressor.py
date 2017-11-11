from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data_set=load_iris()

X_train, X_test, y_train, y_test = train_test_split(data_set.data, data_set.target, random_state=0)

DecReg=DecisionTreeRegressor()
DecReg.fit(X_train, y_train)

print("Accuracy of Training data: {:.5f}".format(DecReg.score(X_train, y_train)))
print("Accuracy of Testing data: {:.5f}".format(DecReg.score(X_test, y_test)))

results = DecReg.predict(X_test)

for i in range(len(results)):

	if int(results[i]) == int(y_test[i]):
		print(True)
	else:
		print(False) 