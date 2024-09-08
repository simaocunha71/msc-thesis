def amicable_numbers_sum(n):
    def divisor_sum(num):
        return sum([i for i in range(1, num) if num % i == 0])

    amicable_numbers = []
    for i in range(2, n+1):
        if divisor_sum(i) != i and divisor_sum(divisor_sum(i)) == i:
            amicable_numbers.append(i)

    return sum(amicable_numbers)