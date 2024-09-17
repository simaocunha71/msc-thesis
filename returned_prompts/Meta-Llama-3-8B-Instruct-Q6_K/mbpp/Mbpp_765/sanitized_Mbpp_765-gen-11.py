def is_polite(n):
    def sum_divisors(x):
        return sum(i for i in range(1, x) if x % i == 0)

    polite_numbers = []
    i = 1
    while len(polite_numbers) < n:
        if sum_divisors(i) == i:
            polite_numbers.append(i)
        i += 1
    return polite_numbers[-1]