To solve this problem, we can follow these steps:

1. Check if all the three numbers are integers or not. If any of them are not integers, return False. To check if a number is an integer, we can use the is_integer() function from the math module. This function returns True if the number is an integer, and False otherwise.

2. If all the numbers are integers, then check if one of them is equal to the sum of the other two. To do this, we can use a loop to iterate through the numbers and check if any of them is equal to the sum of the other two. If we find such a number, return True. Otherwise, return False.

Here's the code that implements the above steps:

```python
import math

def any_int(x, y, z):
    # Step 1: Check if all the numbers are integers
    if not math.is_integer(x) or not math.is_integer(y) or not math.is_integer(z):
        return False

    # Step 2: Check if one of the numbers is equal to the sum of the other two
    if x == (y + z) or y == (x + z) or z == (x + y):
        return True
    else:
        return False
```

You can test the function with the provided examples:

```python
print(any_int(5, 2, 7))  # True
print(any_int(3, 2, 2))  # False
print(any_int(3, -2, 1))  # True
print(any_int(3.6, -2.2, 2))  # False
```

The function will return True if one of the numbers is equal to the sum of the other two, and all numbers are integers. Otherwise, it will return False.

Note: The is_integer() function from the math module is available in Python 3. In Python 2, you can use the int() function to check if a number is an integer.

I hope this helps! Let me know if you have any more questions.

```python

```

Answer: The provided Python function `any_