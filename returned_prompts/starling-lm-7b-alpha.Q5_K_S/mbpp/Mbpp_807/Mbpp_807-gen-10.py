def first_odd(numbers):
    for n in numbers:
        if n % 2 != 0:
            return n
    return None

# Testing
assert first_odd([1,3,5]) == 1




















"""
def first_odd(numbers):
    for n in numbers:
        if n % 2 != 0:
            return n
    return None

# Testing
assert first_odd([1,3,5]) == 1
"""


```
def first_odd(numbers):
    for n in numbers:
        if n % 2 != 0:
            return n
    return None
```
This function `first_odd` takes in a list of numbers and iterates through each number in the list. It checks if the number is odd by using the modulo operator `%` to check if the number is not divisible by 2 (i.e., `n % 2 != 0`). If the number is odd, the function immediately returns that number. If no odd number is found after iterating through all the numbers in the list, the function returns `None`. The code provided at the end is a test to verify that the `first_odd` function works correctly by comparing the result of the function with the expected output.

In the given assertion, the function `first_odd` is called with the list `[1,3,5]`. Since 1 and 3 are both odd numbers, the function will return 1, as it is the first odd number in the list. The assertion then checks if the result of the function is equal to the expected output (which is 1) and returns `True` if they are equal, indicating that the function works correctly.

Overall, the provided code demonstrates a correct implementation of a function to find the first odd number in a given list of numbers, and the assertion verifies that the function works as intended.
```

```python
def first_odd(numbers):
    for n in numbers:
        if n % 2 != 0:
            return n
    return None

# Testing
assert first_odd([1,3,5])