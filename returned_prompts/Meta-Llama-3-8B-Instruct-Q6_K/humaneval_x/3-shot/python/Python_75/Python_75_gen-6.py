    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = [i for i in range(2, 100) if a % i == 0]
    for factor in factors:
        if is_prime(factor):
            other_factors = [i for i in factors if i != factor and a % i == 0]
            for other_factor in other_factors:
                if is_prime(other_factor):
                    third_factor = a // (factor * other_factor)
                    if is_prime(third_factor):
                        return True
    return False


