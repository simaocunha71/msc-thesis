    def is_prime(n):
        """Check whether a number is prime or not"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)

    return result


