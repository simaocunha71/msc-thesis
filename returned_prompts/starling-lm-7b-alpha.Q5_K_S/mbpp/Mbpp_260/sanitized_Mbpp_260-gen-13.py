def newman_prime(n):
    if n == 1:
        return 2
    else:
        a = 2
        while True:
            a = (a ** 2) % (2 ** n)
            if a == 1:
                continue
            d = 2
            while True:
                a = (a ** 2) % (2 ** n)
                if a == 1:
                    break
                if d % 2 == 0:
                    a = (a ** (d // 2)) % (2 ** n)
                d += 1
            if d == 2 ** n:
                return a