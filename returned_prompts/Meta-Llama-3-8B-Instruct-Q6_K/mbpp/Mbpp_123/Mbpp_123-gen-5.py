```
def amicable_numbers_sum(n):
    def sum_factors(x):
        return sum(i for i in range(1, x) if x % i == 0)

    def is_amicable(x):
        return sum_factors(sum_factors(x)) == x and x != sum_factors(x)

    return sum(i for i in range(1, n+1) if is_amicable(i))
```
The amicable numbers are two different numbers so that the sum of the proper divisors of each is equal to the other number. A proper divisor of a number is a divisor that is less than the number itself.

The function `sum_factors(x)` calculates the sum of all proper divisors of `x`.

The function `is_amicable(x)` checks if `x` is an amicable number. It calculates the sum of the proper divisors of `x` and checks if it equals `x` and if `x` is not equal to the sum of its proper divisors.

The function `amicable_numbers_sum(n)` calculates the sum of all amicable numbers from 1 to `n`. It does this by iterating over all numbers from 1 to `n` and checking if each number is an amicable number. If it is, it adds it to the sum. The result is the sum of all amicable numbers from 1 to `n`.

The unit test `assert amicable_numbers_sum(999)==504` checks if the function `amicable_numbers_sum(999)` returns `504`, which is the correct sum of all amicable numbers from 1 to 999.