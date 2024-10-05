    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        while not is_prime(a):
            a, b = b, a + b

    return a


