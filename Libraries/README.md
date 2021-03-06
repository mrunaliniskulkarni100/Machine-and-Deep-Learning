# Important Libraries

## Basic Libraries

Here are some Libraries you'll have to install no matter what other Library you plan to work on. All major libraries such as TensorFlow, Keras, Gym are dependent on these Libraries.

### Numpy

[NumPy](http://www.numpy.org/) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

Install `numpy` and its other dependencies using:

#### For Python 2.n:

`python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose`

#### For Python 3.n:

`python3 -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose`

This command will also install libraries `scipy`, `matplotlib`, `ipython`, `jupyter`, `pandas`, `sympy` and `nose`.

### Scipy

[Scipy](https://www.scipy.org/) is an open source Python Library used for scientific and technical computing.

Scipy contains modules for optimization, linear algebra, integration, interpolation, special functions, Fast Fourier Transform, signal and Image Processing.

To install `scipy`, look at the Numpy Section, or,

#### For Python 2.n:

`pip install scipy`

#### For Python 3.n:

`pip3 install scipy`

### Matplotlib 

[Matplotlib](https://matplotlib.org/) is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shell, the jupyter notebook, web application servers, and four graphical user interface toolkits.

To install `matplotlib`, look at the Numpy Section, or,

#### For Python 2.n:

`pip install matplotlib`

#### For Python 3.n:

`pip3 install matplotlib`

### iPython

[IPython](https://ipython.org/) is a command shell for interactive computing in multiple programming languages, originally developed for the Python programming language, that offers introspection, rich media, shell syntax, tab completion, and history.

To install `ipython`, look at the Numpy Section, or,

#### For Python 2.n:

`pip install ipython`

#### For Python 3.n:

`pip3 install ipython`

### Jupyter Notebook

[The Jupyter Notebook](http://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

To install `jupyter`, look at the Numpy Section, or,

#### For Python 2.n:

`pip install jupyter`

#### For Python 3.n:

`pip3 install jupyter`

### Pandas

In computer programming, [pandas](http://pandas.pydata.org/) is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.

To install `pandas`, look at the Numpy Section, or,

#### For Python 2.n:

`pip install pandas`

#### For Python 3.n:

`pip3 install pandas`

### Sympy

[SymPy](http://www.sympy.org/en/index.html) is a Python library for symbolic computation. It provides computer algebra capabilities either as a standalone application, as a library to other applications, or live on the web as SymPy Live or SymPy Gamma.

To install `sympy`, look at the Numpy Section, or,

#### For Python 2.n:

`pip install sympy`

#### For Python 3.n:

`pip3 install sympy`

Or,

`git clone git://github.com/sympy/sympy.git`

and then,

`python setup.py install`

### Nose 

[Nose](http://nose.readthedocs.io/en/latest/) has been in maintenance mode for the past several years and will likely cease without a new person/team to take over maintainership. New projects should consider using Nose2, py.test, or just plain unittest/unittest2.

To install `nose`, look at the Numpy Section, or, 

run the command,

#### For Python 2.n:

`pip install nose`

#### For Python 3.n:

`pip3 install nose`

### Scikit-Learn

[Scikit-learn](http://scikit-learn.org/stable/) (formerly scikits.learn) is a free software machine learning library for the Python programming language.[3] It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.

To install Sci-kit Learn, run command,

#### For Python 2.n:

`pip install --user --install-option="--prefix=" -U scikit-learn`

#### For Python 3.n:

`pip3 install --user --install-option="--prefix=" -U scikit-learn`

### Pydotplus

PyDotPlus is an improved version of the old pydot project that provides a Python Interface to Graphviz’s Dot language.

#### For Python 2.n:

`pip install pydotplus`

#### For Python 3.n:

`pip3 install pydotplus`

Development Page: [GitHub](https://github.com/carlos-jenkins/pydotplus)

### mglearn

A Library used for plotting and data loading. This library was developed for the [Introduction to Machine Learning with Python: A Guide for Data Scientists](https://www.amazon.in/Introduction-Machine-Learning-Python-Scientists/dp/9352134575?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=88e6e93f-6186-4b6a-acbb-07c8fef57a60) Book

To install mglearn, run command,

#### For Python 2.n:

`pip install mglearn`

#### For Python 3.n:

`pip3 install mglearn`

## TensorFlow

TensorFlow is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) communicated between them. The flexible architecture allows you to deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device with a single API. TensorFlow was originally developed by researchers and engineers working on the Google Brain Team within Google's Machine Intelligence research organization for the purposes of conducting machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well.

Installation Instructions:

Without GPU-Support:

1. Python 2.7: `pip install tensorflow`
2. Python 3.n: `pip3 install tensorflow`

With GPU-Support (needs Nvidia GPU):

1. Python 2.7: `pip install tensorflow-gpu`
2. Python 3.n: `pip3 install tensorflow-gpu`

[More Information](https://www.tensorflow.org/install/)

[TensorFlow Home Page](https://www.tensorflow.org/)

## Keras

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation. 

Use Keras if you need a deep learning library that:

1. Allows for easy and fast prototyping (through user friendliness, modularity, and extensibility)
2. Supports both convolutional networks and recurrent networks, as well as combinations of the two
3. Runs seamlessly on CPU and GPU.

To install keras, run command,

#### For Python 2.n:

`pip install keras`

#### For Python 3.n:

`pip3 install keras`

[Keras Home Page](https://keras.io/)

## OpenCV

OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage and is now maintained by Itseez.

[OpenCV Home Page](https://opencv.org)

[Install Instructions for Linux](https://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html)


## Gym

OpenAI Gym is a toolkit for developing and comparing reinforcement learning algorithms.

[Gym's GitHub Page](https://github.com/openai/gym)

You can install `gym` with:

1. `git clone https://github.com/openai/gym.git`

2. `cd gym`

3. `pip install -e`

Or, you can directly install using `pip`:

`pip install gym`

## Universe

OpenAI Universe is a software platform for measuring and training an AI's general intelligence across the world's supply of games, websites and other applications. This is the universe open-source library, which provides a simple Gym interface to each Universe environment.

[Universe's GitHub Page](https://github.com/openai/universe)

You can install `universe` with:

1. `git clone https://github.com/openai/universe.git`

2. `cd universe`

3. Python 2.n: `pip install -e` or for Python 3.n: `pip3 install -e` 

`universe` needs `numpy` for execution, so if any error occurs while installation, go ahead and install `numpy`, using,

`pip install numpy`

## NEAT 

NEAT (NeuroEvolution of Augmenting Topologies) is a method developed by Kenneth O. Stanley for evovling arbitrary neural networks. 

Install `neat-python` Library using `pip`

#### For Python 2.n:

`pip install neat-python`

#### For Python 3.n:

`pip3 install neat-python`

Or, you can install it from source.

1. `git clone https://github.com/CodeReclaimers/neat-python.git`

2. For Python 2.n: `python setup.py install` or for Python 3.n: `python3 setup.py install`

[NEAT Python's GitHub Page](https://github.com/CodeReclaimers/neat-python)

[neat-python Documentation](http://neat-python.readthedocs.io/en/latest/)