def is_woodall(n):
    def factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def sum_of_factors(n):
        return sum(factors(n))

    return sum_of_factors(n) == n