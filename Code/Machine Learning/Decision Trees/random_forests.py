from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons, load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz

X, y = make_moons(n_samples=100, noise=0.25, random_state=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

forest = RandomForestClassifier(n_estimators=5, random_state=2)
forest.fit(X_train, y_train)

print("Accuracy of Training data: {:.5f}".format(forest.score(X_train, y_train)))
print("Accuracy of Testing data: {:.5f}".format(forest.score(X_test, y_test)))

import pydotplus

for i in range(len(forest.estimators_)):
	graph=pydotplus.graph_from_dot_data(export_graphviz(forest.estimators_[i], out_file=None))
	graph.write_png('random_forest_tree_' + str(i) + '.png')

dataset=load_iris()

X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target)

forest = RandomForestClassifier(n_estimators=100, random_state=2)
forest.fit(X_train, y_train)

print("Accuracy of Training data: {:.5f}".format(forest.score(X_train, y_train)))
print("Accuracy of Testing data: {:.5f}".format(forest.score(X_test, y_test)))

import pydotplus

for i in range(len(forest.estimators_)):
	graph=pydotplus.graph_from_dot_data(export_graphviz(forest.estimators_[i], out_file=None))
	graph.write_png('random_forest_tree_' + str(i) + '.png')