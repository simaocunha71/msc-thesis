Here is a Python solution using a helper function to check if a number is prime:

```python
def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = max([x for x in lst if is_prime(x)])
    return sum(int(digit) for digit in str(max_prime))
```

This function first defines a helper function `is_prime` to check if a number is prime. It then finds the maximum prime number in the list using a list comprehension and the `max` function. Finally, it converts the maximum prime number to a string, iterates over the digits, converts each digit back to an integer, and returns the sum of these digits.