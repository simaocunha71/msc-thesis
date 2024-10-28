    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
            if is_prime(a):
                return a


