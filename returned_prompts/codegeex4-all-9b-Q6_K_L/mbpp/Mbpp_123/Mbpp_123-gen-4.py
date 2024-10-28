def amicable_numbers_sum(n: int) -> int:
    def sum_of_divisors(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum

    amicable_sum = 0
    for i in range(1, n+1):
        j = sum_of_divisors(i)
        if sum_of_divisors(j) == i and i != j:
            amicable_sum += i + j

    return amicable_sum