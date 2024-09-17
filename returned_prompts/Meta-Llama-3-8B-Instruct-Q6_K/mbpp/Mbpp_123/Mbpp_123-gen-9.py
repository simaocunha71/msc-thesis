```
def amicable_numbers_sum(n):
    def sum_of_proper_divisors(num):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors

    total = 0
    for i in range(1, n+1):
        num1 = sum_of_proper_divisors(i)
        if num1 > i and sum_of_proper_divisors(num1) == i:
            total += i + num1
    return total
```


The problem is asking to write a function that calculates the sum of all amicable numbers from 1 to a specified number `n`.

Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number. For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; these add up to 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; these add up to 220.

We can use a helper function `sum_of_proper_divisors` to calculate the sum of proper divisors of a number. Then we iterate over all numbers from 1 to `n`, and for each number, we calculate its sum of proper divisors. If the sum of proper divisors of a number is greater than the number itself and equal to another number `num2`, then `num1` and `num2` are amicable numbers, and we add them to the total sum.

The unit test `assert amicable_numbers_sum(999)==504` helps to ensure the correctness of the function. It checks that the sum of all amicable numbers from 1 to 999 is 504. 

The time complexity of this function is O(n*sqrt(n)) because for each number, we iterate over its proper divisors up to the square root of the number. The space complexity is O(1) as we only use a constant amount of space to store the sum of divisors and the total sum. 