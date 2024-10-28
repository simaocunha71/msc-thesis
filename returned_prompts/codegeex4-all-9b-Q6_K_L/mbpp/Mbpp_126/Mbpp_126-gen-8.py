def sum_of_common_divisors(a, b):
    common_divisors = set()
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.add(i)
    return sum(common_divisors)

