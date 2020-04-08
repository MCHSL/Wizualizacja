class Ksztalty:
	# definicja konstruktora
	def __init__(self, x, y):
		# deklarujemy atrybuty
		# self wskazuje że chodzi o zmienne właśnie definiowanej klasy
		self.x = x
		self.y = y
		self.opis = "To będzie klasa dla ogólnych kształtów"

	def pole_prostokatu(self):
		return self.x * self.y

	def obwod(self):
		return 2 * self.x + 2 * self.y

	def dodaj_opis(self, text):
		self.opis = text

	def skalowanie(self, czynnik):
		self.x = self.x * czynnik
		self.x = self.y * czynnik


class Kwadrat(Ksztalty):
	def __init__(self, x):
		self.x = x
		self.y = x

	def __str__(self):
		return 'Kwadrat o boku {}'.format(self.x)

	def __add__(self, other):
		return Kwadrat(self.x + other.x)

	def __ge__(self, other):
		return self.x >= other.x

	def __gt__(self, other):
		return self.x > other.x

	def __le__(self, other):
		return self.x <= other.x

	def __lt__(self, other):
		return self.x < other.x


kw1 = Kwadrat(5)
kw2 = Kwadrat(10)
print(f"Kwadrat 1: {str(kw1)}, Kwadrat 2: {str(kw2)}")
print(f"Suma: {kw1 + kw2}")
if kw1 < kw2:
	print("Kwadrat 1 jest mniejszy od kwadratu 2")
else:
	print("Kwadrat 1 jest wiekszy od kwadratu 2")
