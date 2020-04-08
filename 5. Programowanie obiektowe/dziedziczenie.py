class Material:
	def __init__(self, rodzaj, dlugosc, szerokosc):
		self.rodzaj = rodzaj
		self.dlugosc = dlugosc
		self.szerokosc = szerokosc

	def wyswietl_nazwe(self):
		print(self.rodzaj)


class Ubrania(Material):
	def __init__(self, rozmiar, kolor, dla_kogo):
		self.rozmiar = rozmiar
		self.kolor = kolor
		self.dla_kogo = dla_kogo

	def wyswietl_dane(self):
		print(
		    f"Ubranie {self.rozmiar}, kolor: {self.kolor}, docelowy nosiciel: {self.dla_kogo}"
		)


class Sweter(Ubrania):
	def __init__(self, rodzaj_swetra):
		self.rodzaj_swetra = rodzaj_swetra

	def wyswietl_dane(self):
		print(f"Sweter, {self.rodzaj_swetra}")


grafen = Material("grafen", 50, 50)
grafen.wyswietl_nazwe()

nanorurki = Material("nanorurki", 100, 1)
nanorurki.wyswietl_nazwe()

spodnie = Ubrania("XL", "niebieski", "kazdy")
spodnie.wyswietl_dane()

bluza = Ubrania("M", "czarny", "kanciaste nastolatki")
bluza.wyswietl_dane()

sweter = Sweter("rozpruty")
sweter.wyswietl_dane()
sweter.wyswietl_nazwe()  # :(
