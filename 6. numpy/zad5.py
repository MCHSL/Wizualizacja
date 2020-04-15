import numpy as np


def diagonalna(n):
	wektor = np.arange(n, 0, -1)
	return np.diag(wektor)


print(diagonalna(5))
