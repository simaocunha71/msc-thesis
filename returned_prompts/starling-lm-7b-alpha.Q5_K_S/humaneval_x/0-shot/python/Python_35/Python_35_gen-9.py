
Here's a Python function that solves the problem:

```python
def max_element(l: list):
    return max(l)
```

In this function, the `max()` function is used to find the maximum element in the list. The `max()` function returns the maximum value in an iterable or the maximum of two or more arguments.

To test the function, you can use doctests. Here are some examples:

```python
def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    print("All tests passed!")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

When you run this script, it will print "All tests passed!" if all the tests pass.

This function can be used to find the maximum element in any list of numeric values.

It's important to note that Python's `max()` function only works with numeric values. If you want to find the maximum element in a list of arbitrary values, you can use the `max()` function with a custom key function. Here's an example:

```python
def max_element(l: list, key_function=None):
    if key_function:
        return max(l, key=key_function)
    else:
        return max(l)
```

In this version of the function, the `key_function` parameter is optional. If a key function is provided, it will be used to determine the "maximumness" of the elements. If no key function is provided, it will default to using the built-in `max()` function.

Here are some examples of how you can use this function:

```python
print(max_element([1, 2, 3]))  # Returns 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 12