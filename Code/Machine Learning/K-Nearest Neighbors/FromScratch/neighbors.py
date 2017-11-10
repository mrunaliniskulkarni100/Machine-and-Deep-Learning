from Point import Point
from operator import itemgetter
import numpy as np # To use the random function, which will help in getting the Training and Testing List
import math # For Square and Square Root Functions

# Initialising Training Point List
training_points_list = []
temp = np.random.rand(100, 2)

for i in temp:
	training_points_list.append(Point(i[0], i[1]))

# Similarly, generate Testing Point List
testing_point_list = []
temp = np.random.rand(25, 2)

for i in temp:
	testing_point_list.append(Point(i[0], i[1]))



# Guessing function:
def guess(testing_point, k = 20):
	closest = [] # List of Points in Training set closest to Testing Point
	for i in training_points_list:
		closest.append((i, distance(testing_point, i)))

	closest.sort(key=lambda tup: tup[1])
	temp = []

	for i in range(k):
		temp.append(closest[i])

	closest = temp

	TrueCount = 0
	FalseCount = 0

	for i in closest:
		if i[0].boolean:
			TrueCount += 1
		else:
			FalseCount += 1

	return TrueCount > FalseCount


def distance(pointA, pointB):
	# Using the simple Euclidean function as the distance function. This will vary from dataset to dataset
	return math.sqrt(
			(pointA.x - pointB.x) ** 2
				+
			(pointA.y - pointB.y) ** 2
		)

for i in testing_point_list:
	ret_val = guess(i)


	if ret_val == i.boolean:
		print (str(testing_point_list.index(i)) + " : " +  str(True))
	else:
		print (str(testing_point_list.index(i)) + " : " +  str(False))