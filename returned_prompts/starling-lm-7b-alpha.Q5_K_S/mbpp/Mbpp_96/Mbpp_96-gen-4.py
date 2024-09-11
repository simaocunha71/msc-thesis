"""
def divisor(n):
    if n < 0:
        return 0
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c += 1
    return c
"""

from math import sqrt
def divisor(n):
    if n < 0:
        return 0
    c = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            c += 1
            if i != n / i:
                c += 1
    return c


def test():
    assert divisor(1) == 1
    assert divisor(2) == 2
    assert divisor(3) == 2
    assert divisor(4) == 3
    assert divisor(5) == 2
    assert divisor(6) == 4
    assert divisor(7) == 2
    assert divisor(8) == 4
    assert divisor(9) == 3
    assert divisor(10) == 4
    assert divisor(15) == 4
    assert divisor(20) == 8
    assert divisor(25) == 4
    assert divisor(30) == 8
    assert divisor(50) == 8
    assert divisor(75) == 8
    assert divisor(100) == 8
    assert divisor(120) == 8
    assert divisor(121) == 2
    assert divisor(126) == 12
    assert divisor(140) == 10
    assert divisor(150) == 10
    assert divisor(200) == 16
    assert divisor(225) == 12
    assert divisor(250) == 10
    assert divisor(300) == 12
    assert divisor(350) == 16
    assert divisor(400) == 16
    assert divisor(42