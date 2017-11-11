# Decision Trees

Decision Trees are widely used models for classification and regression tasks. Essentially, they learn a hierarchy of if/else questions, leading to a decision.

Learning a decision tree means learning the sequence of if/else questions that gets us to the true answer more quickly. In the machine learning setting, these questions are called tests. Usually data does not come in the form of binary yes/no features, but instead represented as continuous features such as in 2D dataset.

The code given saves an Image File of the Decision Tree.

## Random Forests

The main drawback of decision trees is that they tend to overfit the training data. Random Forests avoids this. A random forest is essentially a collection of decision trees, where each tree is slightly different from the others. The idea behind random forests is that each tree might do a relatively good job of predicting, but will likely overfit part of the data. If we build many trees, all of which work well and overfit in different ways, we can reduce the amount of overfitting by averaging their results.

## Libraries used:

1. [Sklearn-Learn](http://scikit-learn.org/stable/)
2. [Pydotplus](https://pypi.python.org/pypi/pydotplus)


