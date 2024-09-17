def amicable_numbers_sum(n: int) -> int:
    def sum_of_divisors(num: int) -> int:
        return sum(d for d in range(1, num) if num % d == 0)

    amicable_sum = 0
    for i in range(2, n + 1):
        if sum_of_divisors(i) != i and sum_of_divisors(sum_of_divisors(i)) == i:
            amicable_sum += i
    return amicable_sum

