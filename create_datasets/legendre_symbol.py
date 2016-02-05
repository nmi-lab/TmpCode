#!/usr/bin/env python
# -*- coding: utf-8 -*-


def isPrime(a):
    return all(a % i for i in range(2, a))


# http://stackoverflow.com/a/14793082/562769
def factorize(n):
    factors = []
    p = 2
    while True:
        while(n % p == 0 and n > 0):
            factors.append(p)
            n = n / p
        p += 1
        if p > n / p:
            break
    if n > 1:
        factors.append(n)
    return factors


def calculateLegendre(a, p):
    """
    Calculate the legendre symbol (a, p) with p is prime.
    The result is either -1, 0 or 1
    """
    if a >= p or a < 0:
        return calculateLegendre(a % p, p)
    elif a == 0 or a == 1:
        return a
    elif a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    elif a == p-1:
        if p % 4 == 1:
            return 1
        else:
            return -1
    elif not isPrime(a):
        factors = factorize(a)
        product = 1
        for pi in factors:
            product *= calculateLegendre(pi, p)
        return product
    else:
        if ((p-1)/2) % 2 == 0 or ((a-1)/2) % 2 == 0:
            return calculateLegendre(p, a)
        else:
            return (-1)*calculateLegendre(p, a)


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pylab as plt

    n = 20
    max_num = 100

    array = np.empty((n*n, ))
    for i in range(n*n):
        a = np.random.randint(1, max_num)
        b = np.random.randint(1, max_num)
        array[i] = calculateLegendre(a, b)

    plt.imshow(array.reshape(n, n), interpolation='nearest', cmap=plt.cm.gray)
    plt.show()
