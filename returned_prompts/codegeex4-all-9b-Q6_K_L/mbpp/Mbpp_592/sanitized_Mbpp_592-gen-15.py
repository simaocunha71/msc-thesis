def sum_Of_product(n: int) -> int:
    co_eff = [1]
    for i in range(1, n+1):
        co_eff.append((co_eff[-1] * (n-i+1)) // i)
    return sum(i*j for i, j in zip(co_eff, co_eff[1:]))