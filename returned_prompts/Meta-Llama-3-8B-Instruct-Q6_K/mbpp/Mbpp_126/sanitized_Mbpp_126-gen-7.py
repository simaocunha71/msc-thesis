def sum(a, b):
    a_factors = set(range(1, a+1))
    b_factors = set(range(1, b+1))
    common_factors = a_factors & b_factors
    return sum(common_factors) - a - b