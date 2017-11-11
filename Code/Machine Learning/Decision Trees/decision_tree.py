from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pydotplus
import collections

clf=DecisionTreeClassifier(random_state=0)
iris=load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

clf=clf.fit(X_train, y_train)

graph=pydotplus.graph_from_dot_data(export_graphviz(clf, out_file=None))
graph.write_png('tree.png')

print ("Accuracy on training set: {:.5f}".format(clf.score(X_train, y_train)))
print ("Accuracy on testing set: {:.5f}".format(clf.score(X_test, y_test)))