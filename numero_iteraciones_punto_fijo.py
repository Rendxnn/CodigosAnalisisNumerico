import math

def numero_iteraciones_punto_fijo(gpx, x0, a, b, tol):
	return (math.log2(tol / max(x0 - a, b - x0))) / (math.log2(gpx))


if __name__ == "__main__":
	x0 = -0.5
	gpx = 0.7
	a, b = -3, -1
	tol = 0.5e-3
	print(numero_iteraciones_punto_fijo(gpx, x0, a, b, tol))