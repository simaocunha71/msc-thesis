```
def amicable_numbers_sum(n):
    def sum_divisors(num):
        return sum(i for i in range(1, num) if num % i == 0)

    def is_amicable(a, b):
        if a != b and sum_divisors(a) == b and sum_divisors(b) == a:
            return True
        return False

    total_sum = 0
    for i in range(1, n):
        for j in range(i, n):
            if is_amicable(i, j):
                total_sum += i + j
    return total_sum
```


This function first defines two helper functions: `sum_divisors` to calculate the sum of divisors for a number, and `is_amicable` to check if two numbers are amicable. It then iterates over all numbers from 1 to `n`, and for each number, it checks all numbers from itself to `n` to see if they are amicable. If they are, it adds their sum to the total sum. The function returns the total sum of all amicable numbers.

The unit test `assert amicable_numbers_sum(999)==504` shows that the function should sum all amicable numbers from 1 to 999, which is 504.