import math


def busquedas_incrementales(x0, deltax, niter):
	i = 0
	print(f'i\t\tx0\t\tx1\t\tfx0\t\tfx1\t\tCambioSigno')
	while i < niter:
		x1 = x0 + deltax
		fx0 = f(x0)
		fx1 = f(x1)
		print(f'{i}\t\t{x0}\t\t{x1}\t\t{fx0}\t\t{fx1}\t\t{fx1 * fx0 < 0}')

		i += 1
		x0 = x1

		if fx1 * fx0 < 0:
			return #VERIFICARRRRRRRRRRRRRRRRRRRRRRR

	return

def f(x):
	#Poner funcion
	return math.exp(-x) + x**2 - 13


if __name__ == "__main__":
	x0 = 1
	deltax = 0.5
	niter = 10
	busquedas_incrementales(x0, deltax, niter)