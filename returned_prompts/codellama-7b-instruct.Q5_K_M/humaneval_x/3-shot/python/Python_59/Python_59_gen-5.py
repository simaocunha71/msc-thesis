    while True:
        for p in range(int(n ** 0.5), 1, -1):
            if n % p == 0:
                return p

        return n


