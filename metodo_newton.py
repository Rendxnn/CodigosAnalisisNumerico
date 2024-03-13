import sympy as sp

def newton(x0, f, tol, niter):
    i = 0
    df = f.diff()
    E = float('inf')
    print(f'i\t\tx0\t\tx1\t\tE')
    while E > tol and i < niter:
        x1 = x0 - f.subs('x', x0) / df.subs('x', x0)
        x1 = x1.evalf()
        E = abs(x1 - x0)
        print(f'{i}\t\t{x0}\t\t{x1}\t\t{E}')

        i += 1
        x0 = x1

if __name__ == "__main__":
    x = sp.Symbol('x')
    f = sp.exp(x) / x + 3
    x0 = -1
    tol = 0.5e-7
    niter = 1000
    newton(x0, f, tol, niter)
