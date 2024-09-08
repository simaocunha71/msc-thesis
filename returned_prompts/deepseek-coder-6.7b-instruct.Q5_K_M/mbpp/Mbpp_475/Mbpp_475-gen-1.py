Here is a Python solution using the built-in sorted function:

```python
def sort_counter(dict):
    return sorted(dict.items(), key=lambda item: item[1])

print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))
```

This function uses the `sorted` method to sort the items of the dictionary, which are tuples of the form `(key, value)`. The `key` argument is a function that takes an item and returns a value by which to sort the items. In this case, we use a lambda function that simply returns the value of each item. 

The result is a list of tuples, where each tuple is a key-value pair from the original dictionary, sorted in ascending order by value.

Note: The built-in `sorted` function in Python maintains the order of items with equal sort keys (i.e., items with equal values). So, the output will maintain the original order of items with equal values.

If you want to sort in descending order, you can add `reverse=True` to the `sorted` function call like this:

```python
def sort_counter(dict):
    return sorted(dict.items(), key=lambda item: item[1], reverse=True)

print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))
```

This will sort the items in descending order by value.
"""