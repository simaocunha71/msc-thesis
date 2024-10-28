To solve this problem we can follow these steps:

1. Check if all the given numbers are integers. If any of them is not an integer, return False. This is because the problem statement clearly states that all the numbers should be integers. We can use the `isinstance()` function to check if a variable is an instance of a specific datatype. In this case, we can use `isinstance()` with the `int` datatype to check if the given numbers are integers.

2. If all the given numbers are integers, then we can calculate the sum of two of the numbers. We can use the `+` operator to add the numbers. Then, we can check if the sum is equal to the third number. If the sum is equal to the third number, return True. Otherwise, return False.

Here's the Python code that implements the above steps:

```python
def any_int(x, y, z):
    # Step 1: Check if all the given numbers are integers
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False

    # Step 2: Check if the sum of two numbers is equal to the third number
    if x + y == z or y + z == x or z + x == y:
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

These test cases should return the expected output.

The function works by first checking if all the input numbers are integers using the `isinstance()` function. If any of them are not integers, it immediately returns False. If all the numbers are integers, it then checks if the sum of two of the numbers is equal to the third number. If the sum is equal to the third number, it returns True. Otherwise, it returns False.

This solution ensures that the function follows