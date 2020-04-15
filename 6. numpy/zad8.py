import numpy as np


def przetnij(macierz, kierunek):
	#kierunek: 0 - pionowo, 1 - poziomo
	if kierunek == 0:
		if macierz.shape[1] % 2 != 0:
			raise Exception(
			    "Nie mozna podzielic pionowo na pol macierzy z nieparzysta iloscia kolumn"
			)
		return np.hsplit(macierz,
		                 2)  # Ciekawe, ze hsplit dzieli macierz pionowo

	elif kierunek == 1:
		if macierz.shape[0] % 2 != 0:
			raise Exception(
			    "Nie mozna podzielic poziomo na pol macierzy z nieparzysta iloscia wierszy"
			)
		return np.vsplit(macierz, 2)

	raise Exception("Nieprawidlowy kierunek")


m = np.array([
    [1, 1, 1, 2, 2, 2],
    [1, 1, 1, 2, 2, 2],
    [3, 3, 3, 4, 4, 4],
    [3, 3, 3, 4, 4, 4],
])

print("Macierz: ")
print(m)
ml, mp = przetnij(m, 0)
mg, md = przetnij(m, 1)
print("Lewa polowa:")
print(ml)
print("Prawa polowa:")
print(mp)
print("Gorna polowa:")
print(mg)
print("Dolna polowa:")
print(md)
