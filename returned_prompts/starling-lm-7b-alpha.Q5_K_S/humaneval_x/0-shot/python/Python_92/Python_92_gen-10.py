To solve this problem, we need to check if the sum of any two numbers is equal to the third number. We also need to ensure that all the numbers are integers. We can use the `isinstance()` function to check if a variable is of a specific type, and the `sum()` function to calculate the sum of a list of numbers. Here's the solution:

```python
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x+y) == z or (y+z) == x or (z+x) == y:
            return True
    return False
```

In this function, we first check if all three variables are integers using the `isinstance()` function. If they are, we then calculate the sum of any two numbers and check if the sum is equal to the third number. If the condition is met, we return `True`, otherwise we return `False`.

You can test this function by calling it with different values, like this:

```python
print(any_int(5, 2, 7))  # True
print(any_int(3, 2, 2))  # False
print(any_int(3, -2, 1))  # True
print(any_int(3.6, -2.2, 2))  # False
```

These test cases should return the expected results as described in the problem.

This solution ensures that all the numbers are integers and checks if any of the numbers is equal to the sum of the other two. If the conditions are met, it returns `True`, otherwise it returns `False`.

The time complexity of this function is O(1), as it only performs a few arithmetic operations and a few type checks.

The space complexity is O(1), as it uses a constant amount of space to store the input variables.

Overall, this function is a simple and efficient solution to the problem, and it meets the requirements described in the problem statement.

```python
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if