import itertools


class Wspak:
	"""Iterator zwracający wartości w odwróconym porządku"""
	def __init__(self, data):
		self.data = data
		self.index = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]


for i in Wspak([1, 2, 3, 4, 5]):
	print(i, end="")
print()
rev_hello = list(Wspak("Hello, world!"))
print(rev_hello)


class Parzyste:
	"""Iterator zwracający parzyste indeksy"""
	def __init__(self, data):
		self.data = data
		self.index = -2

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.data):
			raise StopIteration
		self.index += 2
		if self.index >= len(self.data):  # :/
			raise StopIteration
		return self.data[self.index]


print(list(Parzyste([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


class Samogloski:
	"""Iterator zwracający samogloski w stringach"""
	def __init__(self, data):
		self.data = data
		self.index = -1

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.data):
			raise StopIteration
		self.index += 1
		while self.data[self.index] not in ("a", "e", "i", "o", "u", "y"):
			self.index += 1
			if self.index >= len(self.data):
				raise StopIteration
		return self.data[self.index]


print(list(Samogloski("Witaj swiecie!")))


def znajdz_samogloski(data):
	for c in data:
		if c in ("a", "e", "i", "o", "u", "y"):
			yield c


for sg in znajdz_samogloski("Supercalifragilisticexpialidocious"):
	print(sg, end="")
print()

for combo in itertools.combinations(range(10), 3):
	print(combo, end=" ")
print()


def fibonacci():
	prev = 1
	prevprev = 1
	current = 0
	yield 0
	yield 1
	yield 1
	while True:
		current = prev + prevprev
		prevprev = prev
		prev = current
		yield current


fib = fibonacci()
for i in range(10):
	print(next(fib))


def miesiace():
	for m in ("Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec",
	          "Lipiec", "Sierpien", "Wrzesien", "Pazdziernik", "Listopad",
	          "Grudzien"):
		yield m


print(list(miesiace()))
