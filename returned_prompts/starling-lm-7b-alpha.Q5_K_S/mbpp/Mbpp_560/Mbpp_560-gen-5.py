```
def union_elements(tup1, tup2):
    return sorted(set(tup1 + tup2))
```

The `set(tup1 + tup2)` line creates a set of all unique elements in the two tuples, and the `sorted()` function sorts the set in ascending order.

To use the function, simply call `union_elements` with the two tuples you want to find the union of. For example, to find the union of the elements in `(3, 4, 5, 6)` and `(5, 7, 4, 10)`, you would call `union_elements((3, 4, 5, 6),(5, 7, 4, 10))`. The function will return the union of the elements in sorted order, which in this case would be `(3, 4, 5, 6, 7, 10)`.

Here is the Python code for the function:

```python
def union_elements(tup1, tup2):
    return sorted(set(tup1 + tup2))
```

You can test the function with the example provided:

```python
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
```

This assertion will pass if the function correctly finds the union of the elements in the two tuples and returns them in sorted order.

It's important to note that the `set()` function is used to remove duplicate elements from the union, and the `sorted()` function is used to sort the resulting set in ascending order.

This solution provides a simple and efficient way to find the union of elements in two tuples and output them in sorted order.

Here are some additional details about the code:

- The `set()` function is a built-in Python function that creates a set object from an iterable. In this case, the iterable is the concatenated tuple (`tup1 + tup2`). The `set()` function automatically removes duplicate elements