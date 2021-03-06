# a^2 + b^2 = c^2
# triplet => a, b, c consecutive ints, i.e 2, 3, 4
# exactly one triplet where a + b + c = 1000
# find prod(abc)

from math import prod, pow
import timeit

# brute force
def get_triplet_product_bruteforce():
    for a in range(1, 1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if (a + b + c) ==1000:
                    if pow(a, 2) + pow(b, 2) == pow(c, 2):
                            return (prod([a, b, c]))

# if a=2mn, b= m^2-n^2, c= m^2 + n^2
# a + b + c = 1000
# => (2mn) + (m^2 - n^2) + (m^2 + n^2) = 1000
# => 2mn + 2m^2 = 1000
# => 2m(n + m) = 1000
# => divide both sides by 2
# => m(n+m) = 500
def get_triplet_product():
    for n in range(1, 1000):
        for m in range(n, 1000):
            if m * (n + m) == 500:
                return prod([(2 * m * n), pow(m, 2) - pow(n, 2), pow(m, 2) + pow(n, 2)])

def f():
    for a in range(1,999):
        for b in range(1,999):
            c = (a**2+b**2)**(1/2)
            if c == int(c) and a+b+c == 1000:
                print(a*b*c)
f()
