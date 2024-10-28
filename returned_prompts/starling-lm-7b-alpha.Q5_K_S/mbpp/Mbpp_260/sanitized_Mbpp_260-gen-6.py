def newman_prime(n):
    a, b, c, d = 2, 3, 5, 7
    for _ in range(n):
        a, b, c, d = (a + b) % c, (b + c) % d, (c + d) % a, (d + a) % b
    return d