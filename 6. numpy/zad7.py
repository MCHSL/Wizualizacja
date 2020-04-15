import numpy as np


def dziwna_macierz(n):
	macierz = []
	current_wiersz = []
	for i in range(2, 2 * n + 1, 2):
		current_wiersz.append(i)
	macierz.append(current_wiersz)
	dlugosc_prefixu = 1
	for _ in range(n - 1):
		current_wiersz = []
		for i in range(dlugosc_prefixu, 0, -1):
			current_wiersz.append(i * 2 + 2)
		for i in range(1, n - dlugosc_prefixu + 1):
			current_wiersz.append(i * 2)
		macierz.append(current_wiersz)
		dlugosc_prefixu += 1

	return np.array(macierz)


print(dziwna_macierz(5))
