"""
def count_Primes_nums(n):
    count = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
    return count
"""

def count_Primes_nums(n):
    count = 0
    for i in range(2, n + 1):
        if all(i % j != 0 for j in range(2, i)):
            count += 1
    return count

assert count_Primes_nums(5) == 2



```

In this solution, we are using a function called `count_Primes_nums` that takes in a non-negative number as an argument. Inside the function, we initialize a variable `count` to keep track of the number of prime numbers. Then, we use a for loop to iterate through all numbers from 2 to the given non-negative number. For each number `i`, we use another for loop to check if `i` is divisible by any number in the range from 2 to `i`. If `i` is divisible by any of these numbers, we break out of the inner loop. Otherwise, if the inner loop completes without finding any divisors for `i`, we increment the `count` variable. Finally, we return the `count` variable as the result.

To test the function, we use the `assert` statement to check if the function returns the expected result when given the input `5`. In this case, the expected result is 2, as there are two prime numbers (2 and 3) less than 5. If the assertion passes, it means that the function is working correctly and returning the expected result for the given input.

Overall, this solution provides a way to count the number of prime numbers less than a given non-negative number using a Python function.

```python
```