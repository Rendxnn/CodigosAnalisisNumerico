import math


def numero_iteraciones_biseccion(Xv, Xmn, a, b):

	E = abs(Xmn - Xv)

	n = math.log2((b - a) / E)

	return n



def main():
	Xv = -3.1415
	Xmn = -3.1418
	a, b = -4, 0
	print(numero_iteraciones_biseccion(Xv, Xmn, a, b))


if __name__ == "__main__":
	main()