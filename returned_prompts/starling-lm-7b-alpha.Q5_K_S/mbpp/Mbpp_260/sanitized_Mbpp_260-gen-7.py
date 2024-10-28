def newman_prime(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 7
    else:
        if n % 2 == 0:
            return newman_prime(n - 1)
        else:
            a = 2
            while True:
                b = pow(a, (1 << (n - 3)), 1 << (n - 1))
                if b == 1:
                    return newman_prime(n - 1)
                a += 1