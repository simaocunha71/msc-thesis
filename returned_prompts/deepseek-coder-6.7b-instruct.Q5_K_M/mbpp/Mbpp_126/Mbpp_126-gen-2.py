
def sum_common_divisors(num1, num2):
    def divisors(n):
        return set(i for i in range(1, n + 1) if n % i == 0)
    return sum(divisors(num1) & divisors(num2))


