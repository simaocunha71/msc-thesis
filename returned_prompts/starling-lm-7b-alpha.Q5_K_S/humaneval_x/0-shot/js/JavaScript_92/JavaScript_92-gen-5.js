To solve this kata, we need to follow these steps:

1. Check if all the numbers are integers. If any of them is not an integer, return false.
2. Check if one of the numbers is equal to the sum of the other two. If it is, return true. Otherwise, return false.

Here's the Python code to implement the solution:

```python
def anyInt(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    if x == y + z or y == x + z or z == x + y:
        return True
    return False
```

This code checks if the input numbers are integers using the `isinstance()` function. If any of them is not an integer, it immediately returns false. Then it checks if any of the numbers is equal to the sum of the other two using the `==` operator. If it finds a match, it returns true. Otherwise, it returns false.

Here's a test of the function:

```python
print(anyInt(5, 2, 7))  # true
print(anyInt(3, 2, 2))  # false
print(anyInt(3, -2, 1))  # true
print(anyInt(3.6, -2.2, 2))  # false
```

The output of these tests will be `true`, `false`, `true`, and `false`, respectively, which are the expected results.

The time complexity of this function is O(1) because it performs a constant number of operations regardless of the input size.

The space complexity is also O(1) because it uses a constant amount of additional space.

Overall, this function provides an efficient and correct solution to the problem.

*/

anyInt(5, 2, 7) ➞ true
anyInt(3, 2, 2) ➞ false
anyInt(3, -2, 1) ➞ true
anyInt(3.6, -2.2, 2) ➞ false

// This code uses Python's `isinstance()` function