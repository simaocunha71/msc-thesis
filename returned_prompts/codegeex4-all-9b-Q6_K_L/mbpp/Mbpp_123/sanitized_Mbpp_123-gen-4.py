def amicable_numbers_sum(n):
    def is_amicable(a, b):
        return sum(divisors(a)) == b and sum(divisors(b)) == a

    def divisors(n):
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                yield i

    return sum(i for i in range(1, n + 1) if is_amicable(i, sum(divisors(i))))