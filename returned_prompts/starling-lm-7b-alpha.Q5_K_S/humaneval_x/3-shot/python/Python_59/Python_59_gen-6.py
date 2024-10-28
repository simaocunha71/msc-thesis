    while n % 2 == 0:
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n //= i

    return n


