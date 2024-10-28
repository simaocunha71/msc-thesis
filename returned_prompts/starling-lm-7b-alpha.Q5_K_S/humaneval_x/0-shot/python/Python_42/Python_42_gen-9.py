
Here's a Python solution that uses list comprehension to increment each element in the input list by 1:

```python
def incr_list(l: list):
    return [i + 1 for i in l]
```

You can test the function with the provided examples:

```python
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

The `incr_list` function takes a list as input and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over the input list `l` and create a new list by adding 1 to each element. 

For example, if you call `incr_list([1, 2, 3])`, it will return `[2, 3, 4]` because each element in the input list is incremented by 1. Similarly, if you call `incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])`, it will return `[6, 4, 6, 3, 4, 4, 10, 1, 124]` for the same reason.

The `incr_list` function is a simple and efficient way to increment each element in a list by 1.

```python
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1,