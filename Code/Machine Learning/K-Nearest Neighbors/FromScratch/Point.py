class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

		if (x < y):
			self.boolean = True
		else:
			self.boolean = False

	def display_point(self):
		print (self.x)
		print (self.y)