def sum(a, b):
    def find_divisors(n):
        return [i for i in range(1, n+1) if n % i == 0]

    divisors_a = find_divisors(a)
    divisors_b = find_divisors(b)

    common_divisors = [i for i in divisors_a if i in divisors_b]
    return sum(common_divisors)