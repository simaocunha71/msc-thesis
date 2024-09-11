"""
def newman_prime(n):
    assert 0 < n
    a = 2
    b = 3
    m = 1
    while True:
        a, b = b, (b*b + 1) % a
        m += 1
        if m % n == 0:
            return a
"""

def newman_prime(n):
    assert 0 < n
    a = 2
    b = 3
    m = 1
    while True:
        a, b = b, (b*b + 1) % a
        m += 1
        if m % n == 0:
            return b



# assert newman_prime(3) == 7
# assert newman_prime(100) == 227838830373
# assert newman_prime(2) == 2
# assert newman_prime(1) == 2
# assert newman_prime(10) == 101
# assert newman_prime(9) == 1007
# assert newman_prime(8) == 1006
# assert newman_prime(7) == 997
# assert newman_prime(6) == 991
# assert newman_prime(5) == 983
# assert newman_prime(4) == 977
# assert newman_prime(3) == 7
# assert newman_prime(2) == 2


print(newman_prime(3))
print(newman_prime(100))
print(newman_prime(2))
print(newman_prime(1))
print(newman_prime(10))
print(newman_prime(9))
print(newman_prime(8))
print(newman_prime(7))
print(newman_prime(6))
print(newman_prime(5))
print(newman_prime(4))
print(newman_prime(3))
print(newman_prime(2))



```