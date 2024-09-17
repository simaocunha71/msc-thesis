The problem is asking you to write a function that finds the minimum value in a given list. However, the list can contain elements of different data types, including strings and numbers.

The unit test `assert min_val(['Python', 3, 2, 4, 5, 'version'])==2` suggests that the function should return the smallest number in the list.

Here's a Python solution using the built-in `min` function with a generator expression to filter out non-numeric values:

```
def min_val(lst):
    return min(x for x in lst if isinstance(x, (int, float)))
```

This function iterates over the list, checks if each element is an integer or a float using the `isinstance` function, and returns the smallest one. If the list is empty, it will raise a `ValueError`. If you want to handle this case, you can add a simple check:

```
def min_val(lst):
    numbers = [x for x in lst if isinstance(x, (int, float))]
    return min(numbers) if numbers else None
```

This version of the function returns `None` if the list is empty. You can also raise a specific error or return a default value, depending on your requirements.