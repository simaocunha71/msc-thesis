def amicable_numbers_sum(n: int) -> int:
    def sum_divisors(m: int) -> int:
        return sum(i for i in range(1, m) if m % i == 0)

    amicable_sum = 0
    for i in range(1, n+1):
        j = sum_divisors(i)
        if i != j and sum_divisors(j) == i:
            amicable_sum += i

    return amicable_sum

