"""
def opposite_Signs(num1, num2):
    if num1 < 0 and num2 > 0 or num1 > 0 and num2 < 0:
        return True
    else:
        return False
"""

def opposite_Signs(num1, num2):
    return num1 * num2 < 0

# Testing
assert opposite_Signs(1, -2) == True
assert opposite_Signs(1, 2) == False
assert opposite_Signs(-1, -2) == True
assert opposite_Signs(0, 0) == False
print("All tests pass")

# Time complexity: O(1)
# Space complexity: O(1)

"""
Explanation:

The time complexity and space complexity are O(1) because the function uses only a few
constants and does not depend on the size of the input.

The function `opposite_Signs` uses the property that the product of two integers is negative if and only if they have opposite signs.

In the `if` statement, we check if `num1` and `num2` have opposite signs by checking if the product of `num1` and `num2` is less than 0. If it is, we return True; otherwise, we return False.

In the `else` statement, we return False if the `if` statement condition is not met, indicating that the two integers do not have opposite signs.

By using the property that the product of two integers is negative if and only if they have opposite signs, we can determine whether the two integers have opposite signs in constant time, regardless of the size of the input.

The space complexity is O(1) because the function does not depend on the size of the input, and it only uses a few constants.

In summary, the function `opposite_Signs` has a time complexity of O(1) and a space complexity of O(1), making it efficient for determining whether two integers have opposite signs.
"""

```

```

```

```python

```

```

```python

```

```

```

```

```

``