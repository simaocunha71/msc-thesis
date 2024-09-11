```
def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
```

This function starts by initializing a variable `count` to 0. Then, it loops through each integer `i` from 1 to `n+1`. For each `i`, it checks if `n` is divisible by `i` (i.e., if `n % i == 0`). If it is, the `count` is incremented by 1. Finally, the function returns the value of `count`, which represents the number of divisors of the given integer `n`.

To test the function, you can use the `assert` statement followed by the expected output for a specific input. In this case, the assertion `assert divisor(15) == 4` checks if the function returns 4 when given the input 15. If the assertion is true, it means the function is correct.

Overall, this solution provides a way to find the number of divisors of a given integer in Python.

```python
def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

assert divisor(15) == 4
```

This Python function counts the number of divisors of a given integer by iterating through all the integers from 1 to `n+1` and checking if each integer is a divisor of `n`. The count of divisors is updated for each divisor found. Finally, the function returns the count of divisors.

To test the function, you can use the `assert` statement followed by the expected output for a specific input. In this case, the assertion `assert divisor(15) == 4` checks if the function correctly returns 4 when given the input 15. If the assertion is true, it means the function is correct.

In summary, this Python solution provides a method to find the number of divisors of a given integer using a loop and conditional statements.

```python
def divisor(n):
   