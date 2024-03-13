import math


def f(x):
	return (math.exp(x) / x) + 3 


def g(x):
	return -(math.exp(x) / 3)


def punto_fijo(x0, niter, tol, E=float('inf')):
	print(f'i\t\tx1\t\tfx1\t\tE')
	i = 0
	while i < niter and E > tol:
		x1 = g(x0)
		fx1 = f(x1)
		E = abs(x1 - x0)
		print(f'{i}\t\t{x1}\t\t{fx1}\t\t{E}')
		i += 1
		x0 = x1
	return 


def main():
	x0 = -1
	niter = 1000
	E = 0.5e-7

	punto_fijo(x0, niter, E)


if __name__ == '__main__':
	main()