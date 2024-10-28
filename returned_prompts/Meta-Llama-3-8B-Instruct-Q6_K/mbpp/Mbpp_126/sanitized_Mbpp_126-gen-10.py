def sum(a, b):
    a_factors = [i for i in range(1, a + 1) if a % i == 0]
    b_factors = [i for i in range(1, b + 1) if b % i == 0]
    common_factors = set(a_factors) & set(b_factors)
    return sum(common_factors) - a - b + 1