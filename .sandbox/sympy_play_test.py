## can we use sympy to always generate normalized vectors? ##

import sympy

def sq(x): return x**2
def root(x): return x**0.5

a, b, c, d, e, f = sympy.var('a b c d e f')
expr = root(sq(a) + sq(b) + sq(c) + sq(d) + sq(d) + sq(e) + sq(f)) - 1
print sympy.solve(expr, a)
