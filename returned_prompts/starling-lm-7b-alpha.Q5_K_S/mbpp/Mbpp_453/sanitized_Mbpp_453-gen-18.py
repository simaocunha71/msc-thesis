def sumofFactors(n: int) -> int:
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    factors_sum = 0
    for factor in factors:
        if factor % 2 == 0:
            factors_sum += factor
    return factors_sum