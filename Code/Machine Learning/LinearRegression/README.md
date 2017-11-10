# Linear Regression

Linear Regression, or ordinary least squares (OLS), is the simplest and most classic linear method for regression. Linear Regression finds the parameters w and b that minimize the Squared Error between predictions and the true regression targets, y, on the training set. The mean squared error is the sum of the squared differences between the predictions and the true values. Linear regression has no parameters, which is a benefit, but it also has no way to control model complexity.

# Ridge Regression

Ridge Regression is also a linear model for regression, so the formula it uses to make predictions is the same one used for ordinary least squares. In ridge regression, though, the coefficients (w) are chosen not only so that they predict well on the training data, but also to fit an additional constraint. We also want the magnitude of coefficients to be as small as possible; in other words, all entries of w should be close to zero. Intuitively, this means each feature should have little effect on the outcome as possible, while still predicting well. This constraint is an example of what is called Regularization. Regularization means explicitly restricting a model to avoid overfitting.

## Libraries Used

1. [Numpy](http://www.numpy.org/)
2. [Sklearn-Learn](http://scikit-learn.org/stable/)