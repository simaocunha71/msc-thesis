To solve this problem we need to check whether the given number is a palindrome and its digits are strictly increasing or strictly decreasing. Here is a step-by-step guide on how to do this:

1. Convert the given number to a string, so we can easily check whether it's a palindrome.
2. Check whether the string is a palindrome: Reverse the string and see if it's equal to the original string.
3. If the string is not a palindrome, return False, as the number is not undulating.
4. Split the string into a list of its digits.
5. Check whether the digits are strictly increasing or strictly decreasing:
   a. If the digits are strictly increasing, return True, as the number is undulating.
   b. If the digits are not strictly increasing but are strictly decreasing, return True, as the number is undulating.
   c. If the digits neither strictly increase nor strictly decrease, return False, as the number is not undulating.
6. Here's the Python code for the function:

```python
def is_undulating(num):
    # Convert the number to a string
    num_str = str(num)

    # Check whether the string is a palindrome
    if num_str != num_str[::-1]:
        return False

    # Split the string into a list of its digits
    digits = [int(d) for d in num_str]

    # Check whether the digits are strictly increasing
    for i in range(1, len(digits)):
        if digits[i] <= digits[i - 1]:
            return False

    # The digits are strictly increasing, so the number is undulating
    return True
```

You can use the `assert` statement to verify the function's correctness:

```python
assert is_undulating(1212121) == True
```

This will pass and print nothing if the assertion is true, or raise an `AssertionError` exception with an error message if the assertion is false.

"""

def is_undulating(num):
    num_str = str(num