def newman_prime(n):
    a, b, c, d = 2, 3, 5, 7
    for _ in range(n):
        a, b, c, d = (a + b) % c, (b + c) % d, (c + d) % a, (d + a) % b
    return d

# assert newman_prime(3) == 7
# print(newman_prime(3))
# print(newman_prime(5))
# print(newman_prime(10))


"""
In mathematics, the Newman–Shanks–Williams method, also known as the Newman–Lehmer method, is a primitivity test for composite numbers. It is an algorithm to determine whether a composite number is a Carmichael number. It is an improvement of the original method of Newman and Shanks.

The Newman–Shanks–Williams method is also used as a primitivity test for elliptic curves defined over a finite field. In this context, an elliptic curve is defined over a finite field F p, where p is a prime number.

The Newman–Shanks–Williams method is also used as a primitivity test for the multiplicative group of the integers modulo p for prime p, that is, for the set {0, 1, ..., p − 1}.

The Newman–Shanks–Williams method is also used as a primitivity test for the multiplicative group of the integers modulo p for prime p, that is, for the set {0, 1, ..., p − 1}.

The Newman–Shanks–Williams method is also used as a primitivity test for the multiplicative group of the integers modulo p for prime p, that is, for the set {0, 1, ..., p − 1}.
"""

"""
The Newman–Shanks–Williams method is also used as a primitivity test for the multiplicative group of the integers modulo p for prime p, that is, for the set {0, 1, ..., p − 1}.

The Newman–Shanks–Williams method is also used as a prim