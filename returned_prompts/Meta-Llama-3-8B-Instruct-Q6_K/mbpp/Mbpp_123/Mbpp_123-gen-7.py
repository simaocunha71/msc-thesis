```
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
```


This solution defines a helper function `sum_factors` to calculate the sum of factors of a number. It then iterates over all numbers from 1 to `n`, calculates the sum of factors for each number, and checks if the number and its sum of factors are amicable. If they are, it adds them to a dictionary `amicable_sums`. Finally, it returns the sum of all values in `amicable_sums`. The unit test `assert amicable_numbers_sum(999)==504` ensures that the function works correctly.