def sum(a, b):
    def find_divisors(n):
        return [i for i in range(1, n+1) if n % i == 0]

    divisors_a = set(find_divisors(a))
    divisors_b = set(find_divisors(b))
    common_divisors = divisors_a & divisors_b
    return sum(common_divisors)  # 1 is included in divisors, so subtract 1