```
def amicable_numbers_sum(n):
    def sum_of_divisors(num):
        return sum([i for i in range(1, num) if num % i == 0])

    def is_amicable(a, b):
        return sum_of_divisors(a) == b and sum_of_divisors(b) == a

    amicable_sum = 0
    for i in range(1, n):
        for j in range(i+1, n):
            if is_amicable(i, j):
                amicable_sum += i + j
    return amicable_sum
```
This function works by first defining a helper function `sum_of_divisors` to calculate the sum of the divisors of a number. Then it defines another helper function `is_amicable` to check if two numbers are amicable. The main function `amicable_numbers_sum` then iterates over all numbers from 1 to `n`, and for each number, it checks all the other numbers to see if they are amicable. If they are, it adds their sum to the total. The function finally returns the total sum of all amicable numbers. 

Note: This function has a time complexity of O(n^2) because it checks every pair of numbers. This could be optimized by only checking numbers up to the square root of `n`, but this would still be O(n^2) because it would still have to check every pair of numbers. 

Also, the unit test `assert amicable_numbers_sum(999)==504` is used to check the correctness of the function. This test checks that the function returns 504 when given the input 999. If the function is correct, this test should pass. 

This function is not very efficient, especially for large inputs, because it has a time complexity of O(n^2). A more efficient solution would be to use a sieve to find all the amicable numbers up to a certain number, and then sum them. This would have a time complexity of O(n log n), which is much faster for large inputs. 

Here is an example of how you could use a sieve to find all the amicable numbers up to a certain number:

```
def amicable_numbers_sum(n):
    sieve = [0] * (n+1)
    for i in range(2, n):
        if sieve[i] == 0:
            for j in range(i, n, i):
                sieve[j] += i
   