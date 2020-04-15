import numpy as np


def macierz(n):
	"""
	Dla n=5 generuje macierz
	[[ 1  2  3  4  5]
	 [ 6  7  8  9 10]
	 [11 12 13 14 15]
	 [16 17 18 19 20]
	 [21 22 23 24 25]]
	"""
	return np.array([np.arange(a, a + n) for a in range(1, n * n, n)])


print(macierz(10))
