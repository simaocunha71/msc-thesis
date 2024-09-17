def amicable_numbers_sum(n):
    amicable_numbers = []
    for i in range(1, n+1):
        sum_of_divisors_i = sum(set(range(1, i+1)))
        sum_of_divisors_j = sum(set(range(1, sum_of_divisors_i+1)))
        if i == sum_of_divisors_j and sum_of_divisors_i != i and sum_of_divisors_i != sum_of_divisors_j:
            amicable_numbers.append(i)
    return sum(amicable_numbers)