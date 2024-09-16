def amicable_numbers_sum(limit):
    amicable_numbers = set()
    for i in range(1, limit + 1):
        d = sum(int(j) for j in str(i))
        if d < i and i % d == 0:
            amicable_numbers.add(i)
            amicable_numbers.add(d)
    return sum(amicable_numbers)

