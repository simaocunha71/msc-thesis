    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    factor = n
    while factor > 1:
        factor -= 1
        if n % factor == 0 and is_prime(factor):
            return factor


