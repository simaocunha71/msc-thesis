
def sum_common_divisors(m, n):
    def divisors(x):
        return set(i for i in range(1, x + 1) if x % i == 0)
    return sum(divisors(m) & divisors(n))


