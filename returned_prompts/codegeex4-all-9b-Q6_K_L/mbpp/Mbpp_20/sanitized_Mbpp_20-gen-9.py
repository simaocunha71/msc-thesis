def is_woodall(n):
    def is_prime(p):
        if p < 2:
            return False
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                return False
        return True

    def sum_of_proper_divisors(p):
        total = 1
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                total += i
                if i != p // i:
                    total += p // i
        return total

    if not is_prime(n):
        return False
    return sum_of_proper_divisors(n) == n