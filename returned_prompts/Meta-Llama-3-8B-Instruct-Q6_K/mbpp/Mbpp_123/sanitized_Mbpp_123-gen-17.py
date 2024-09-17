def amicable_numbers_sum(n):
    def sum_factors(num):
        return sum(i for i in range(1, num) if num % i == 0)

    amicable_sums = {}
    for num in range(1, n + 1):
        sum_of_factors = sum_factors(num)
        if sum_of_factors != num:
            sum_of_factors_of_sum_of_factors = sum_factors(sum_of_factors)
            if sum_of_factors == sum_of_factors_of_sum_of_factors and sum_of_factors != num:
                amicable_sums[num] = sum_of_factors
                amicable_sums[sum_of_factors] = num

    return sum(amicable_sums.values())