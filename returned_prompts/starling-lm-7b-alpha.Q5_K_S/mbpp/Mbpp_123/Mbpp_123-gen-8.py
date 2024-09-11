def amicable_numbers_sum(n):
    amicable_numbers = set()
    for i in range(1, n + 1):
        if i == sum(divisors(i)) - i:
            amicable_numbers.add(i)
    return sum(amicable_numbers)

def divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)
```

The function `amicable_numbers_sum` sums all amicable numbers from 1 to a specified number. It starts by creating an empty set called `amicable_numbers` to store the amicable numbers. It then iterates through all numbers from 1 to the specified number (inclusive). For each number `i`, it checks if the sum of its divisors (excluding `i`) is equal to `i`. If it is, then `i` is an amicable number and it is added to the `amicable_numbers` set. Finally, the function returns the sum of all the amicable numbers in the set.

The function `divisors` is a helper function that calculates all the divisors of a number `n`. It starts by creating an empty set called `divisors`. It then iterates through all numbers from 1 to the square root of `n`. For each number `i`, it checks if `n` is divisible by `i`. If it is, then `i` is a divisor of `n` and it is added to the `divisors` set. After the loop, the function returns the sorted `divisors` set.

To use the `amicable_numbers_sum` function, you can pass a number `n` as an argument. For example, if you want to find the sum of all amicable numbers from 1 to 999, you can call the function like this:

```python
result = amicable_numbers_sum(999)
print(result)  # Output: 