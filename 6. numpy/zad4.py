import numpy as np


def potegi(podstawa, ilosc):
	return np.logspace(1, ilosc, base=podstawa, num=ilosc)


print(potegi(2, 10))
