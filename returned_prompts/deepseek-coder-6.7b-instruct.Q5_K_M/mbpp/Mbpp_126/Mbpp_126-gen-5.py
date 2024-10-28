
def sum(a,b):
    def divisors(n):
        return set(i for i in range(1, n + 1) if n % i == 0)
    return sum(divisors(a) & divisors(b))


