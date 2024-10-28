    from math import sqrt

    def is_prime(n):
        """
        Check if a number is prime
        """
        if n < 2:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        sq = int(sqrt(n))

        for i in range(3, sq + 1, 2):
            if n % i == 0:
                return False

        return True

    res = []
    for i in range(2, n):
        if is_prime(i):
            res.append(i)

    return res


