To solve this problem, you can follow these steps:

1. Create an empty list called `primes` to store the prime numbers found in the list.
2. Iterate through the given list using a for loop. For each number `num` in the list, check if it's a prime number using a helper function `is_prime(num)`. If it's a prime number, add it to the `primes` list.
3. Find the largest prime number in the `primes` list using the `max()` function and assign it to the variable `largest_prime`.
4. Convert `largest_prime` to a string using the `str()` function. Then, iterate through each digit in `largest_prime` using a for loop. For each digit `digit`, add it to the `sum_of_digits` variable.
5. Finally, return the `sum_of_digits` as the result.

Here's the code implementation of the solution:

```python
def skjkasdkd(lst):
    primes = []
    for num in lst:
        if is_prime(num):
            primes.append(num)
    largest_prime = max(primes)
    sum_of_digits = 0
    for digit in str(largest_prime):
        sum_of_digits += int(digit)
    return sum_of_digits
```

You can use the `is_prime(num)` function to check if a number is prime. Here's an implementation of the `is_prime(num)` function:

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

With this implementation, you can now find the largest prime value in the given list and return the sum of its digits.

For example, if you call the function with `lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,3