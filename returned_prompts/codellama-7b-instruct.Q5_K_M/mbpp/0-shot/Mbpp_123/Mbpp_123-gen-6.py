"""
def amicable_numbers_sum(n):
    d = {1: 0}
    def sum_divisors(x):
        if x not in d:
            d[x] = sum(i for i in range(1, x // 2 + 1) if x % i == 0)
        return d[x]
    return sum(i for i in range(1, n + 1) if sum_divisors(i) == i and sum_divisors(sum_divisors(i)) == i)
"""
