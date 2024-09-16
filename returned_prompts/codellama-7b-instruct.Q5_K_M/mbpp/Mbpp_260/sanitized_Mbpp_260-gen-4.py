def newman_prime(n):
    if n <= 3:
        return 2 if n == 2 else 3 if n == 3 else None

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                yield i

    def first_prime_factor(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0 and is_prime(i):
                return i

    def newman_shanks_williams_prime_number(n):
        if n == 1:
            return 2
        elif n == 2:
            return 3
        elif n == 3:
            return 7
        else:
            first_factor = first_prime_factor(n)
            if first_factor is not None:
                return first_factor
            else:
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        return newman_shanks_williams_prime_number(i)

    return newman_shanks_williams_prime_number(n)