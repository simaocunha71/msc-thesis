```
def count(lst):
    total = 0
    for i in lst:
        if i:
            total += 1
    return total
```

Explanation:
This function `count` takes a list as an input and initializes a counter `total` to 0. Then it goes through each item in the list and checks if it is `True`. If the item is `True`, the counter is incremented by 1. Finally, the function returns the total count of `True` values in the list.

The `assert` statement at the top of the code is used to test if the function `count` is working correctly. It checks if the function returns the expected result for the given list `[True, False, True]`, which should be 2. If the function doesn't return the correct result, an error will be raised.

To use the function, simply call it with a list as an argument. For example, `count([True, False, True])` will return 2, as expected.

Note: In Python, the boolean values `True` and `False` are represented by the keywords `True` and `False`, respectively.

To count the number of true booleans in a list, you can use the following function:

```python
def count(lst):
    total = 0
    for i in lst:
        if i:
            total += 1
    return total
```

To test if the function is working correctly, you can use the `assert` statement:

```python
assert count([True, False, True]) == 2
```

This will raise an error if the function doesn't return the expected result for the given list.

To use the function, you can simply call it with a list as an argument. For example:

```python
print(count([True, False, True]))  # Output: 2
```

This will count the number of true booleans in the list `[True, False, True]`, which is 2.

In Python, the boolean values `True` and `False` are represented by the keywords `True` and `False`, respectively.

To count the number of true booleans in a list, you can use