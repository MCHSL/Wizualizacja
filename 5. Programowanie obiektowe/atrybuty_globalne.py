class Point:
	counter = []

	def __init__(self, x=0, y=0):
		"""Konstuktor punktu."""
		self.x = x
		self.y = y

	def update(self, n):
		self.counter.append(n)


p1 = Point(0, 0)
p2 = Point(1, 1)
p3 = Point(2, 2)

print(p1.counter)
print(p2.counter)
print(p3.counter)
p1.update(1)
print(p1.counter == p2.counter)
p3.counter = "AAAAAAAAAAAAAAAAAA"
p1.update(2)
print(p2.counter)
print(p3.counter)
Point.counter = 1337
p1.update(3)
