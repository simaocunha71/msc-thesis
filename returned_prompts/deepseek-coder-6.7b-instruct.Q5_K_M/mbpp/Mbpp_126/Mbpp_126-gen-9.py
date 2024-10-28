
def sum_common_divisors(n, m):
    def divisors(n):
        return set(i for i in range(1, n+1) if n % i == 0)
    return sum(divisors(n) & divisors(m))


