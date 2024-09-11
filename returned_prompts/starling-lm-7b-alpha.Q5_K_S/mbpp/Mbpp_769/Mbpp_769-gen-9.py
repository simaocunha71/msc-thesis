"""
def Diff(list1, list2):
    """
    Returns the difference between two lists, i.e. the elements in the first list that are not in the second.
    """
    return [i for i in list1 if i not in list2]


def test_Diff():
    assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]
    print("All tests passed")

if __name__ == '__main__':
    test_Diff()
"""

In Python, you can use list comprehension to get the difference between two lists, i.e., the elements in the first list that are not in the second. Here is a function that does this:

```python
def Diff(list1, list2):
    """
    Returns the difference between two lists, i.e. the elements in the first list that are not in the second.
    """
    return [i for i in list1 if i not in list2]
```

To test this function, you can use the `assert` keyword to check if the function returns the correct result for a given example:

```python
def test_Diff():
    assert Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]) == [10, 20, 30, 15]
    print("All tests passed")
```

By running this script, you can verify that the `Diff` function works correctly.

Here are some additional notes about the `assert` keyword in Python:

- The `assert` keyword is used to test if a condition is true. If the condition is false, an `AssertionError` is raised. This can be useful for debugging and testing code.
- The `assert` keyword is typically used at the beginning of a test function, like in the example above. If any of the `assert` statements in the function fail, an `AssertionError` is raised, and the function exits immediately.