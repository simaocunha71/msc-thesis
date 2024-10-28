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