import math

def f(x):
    return math.exp(x) / x + 3

def regla_falsa(a, b, niter, tol):
    i = 0
    fc = float('inf')
    print(f'i\t\ta\t\tb\t\txm')
    while i < niter:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)
        print(f'{i}\t\t{a}\t\t{b}\t\t{c}')
        if abs(fc) < tol:
            break
        if f(a) * fc > 0:
            a = c
        else:
            b = c
        i += 1

def main():
    a = -2
    b = -0.1
    niter = 10
    tol = 0.5e-7
    regla_falsa(a, b, niter, tol)

if __name__ == '__main__':
    main()
