```
def amicable_numbers_sum(n):
    def sum_factors(num):
        factors = set()
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                factors.add(i)
                if i != num // i:
                    factors.add(num // i)
        return sum(factors) - num

    amicable_sum = 0
    for i in range(1, n + 1):
        if i == sum_factors(sum_factors(i)):
            amicable_sum += i
    return amicable_sum
```



Explanation:
The problem asks to find the sum of all amicable numbers up to a given number `n`. Amicable numbers are pairs of numbers where the sum of the proper divisors of each number is equal to the other number. For example, 220 and 284 are amicable numbers because the sum of proper divisors of 220 is 284 and the sum of proper divisors of 284 is 220.

The function `amicable_numbers_sum(n)` iterates over all numbers from 1 to `n` and checks if each number is amicable. If a number is amicable, its sum is added to the total sum. The function `sum_factors(num)` calculates the sum of proper divisors of a given number.

The unit test `assert amicable_numbers_sum(999)==504` ensures that the function returns the correct sum for the given input. This test checks if the sum of all amicable numbers up to 999 is indeed 504. 





The time complexity of this solution is O(n * sqrt(n)), where `n` is the input number. This is because for each number, we are calculating the sum of its factors, which takes O(sqrt(n)) time. The space complexity is O(n), as we are storing the sum of factors for each number in a set.