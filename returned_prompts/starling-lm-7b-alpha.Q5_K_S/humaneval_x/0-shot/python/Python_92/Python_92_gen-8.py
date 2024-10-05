To solve this kata, you should:

- Check if all the numbers are integers. If not, return False.
- For each number, check if the sum of the other two numbers is equal to the current number.
- If true, return True. If not, return False.

Here's the Python solution:

```
def any_int(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False

    return any([x == y + z, y == x + z, z == x + y])
```

Here's the explanation of the Python solution:

- The function `isinstance(x, int)` checks if `x` is an integer. If it's not, the function returns False. The same check is performed for `y` and `z`.
- The function `any()` returns True if at least one of the conditions is true. If none of the conditions are true, `any()` returns False.
- The conditions `x == y + z, y == x + z, z == x + y` check if one of the numbers is equal to the sum of the other two.

You can test the function with the following examples:

```
print(any_int(5, 2, 7))  # True
print(any_int(3, 2, 2))  # False
print(any_int(3, -2, 1)) # True
print(any_int(3.6, -2.2, 2))  # False
```

The Python function will correctly identify if one of the numbers is equal to the sum of the other two, and if all the numbers are integers.











































































































