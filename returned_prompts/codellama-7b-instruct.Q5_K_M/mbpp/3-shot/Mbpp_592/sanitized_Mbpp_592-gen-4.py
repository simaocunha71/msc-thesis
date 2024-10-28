def sum_Of_product(n):
    co_eff = [1]
    for i in range(n):
        co_eff.append(co_eff[-1] * (n - i) / (i + 1))
    return sum(co_eff)