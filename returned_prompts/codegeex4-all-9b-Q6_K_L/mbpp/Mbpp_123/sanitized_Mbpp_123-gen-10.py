def amicable_numbers_sum(n):
    def divisor_sum(x):
        return sum(i for i in range(1, x) if x % i == 0)

    amicable_pairs = []
    for i in range(2, n + 1):
        d_i = divisor_sum(i)
        if d_i != i and divisor_sum(d_i) == i:
            amicable_pairs.append((i, d_i))

    return sum(i for i, _ in amicable_pairs)