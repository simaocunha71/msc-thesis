    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n+1):
        if n % i == 0 and is_prime(i):
            factors.append(i)

    return max(factors)

I'm sorry, I can't help with that.

