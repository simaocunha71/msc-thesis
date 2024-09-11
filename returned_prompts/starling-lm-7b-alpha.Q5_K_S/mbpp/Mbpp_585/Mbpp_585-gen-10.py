Here's one way you could approach this problem:

```python
def expensive_items(dataset, n):
    """
    Find the n most expensive items in a given dataset.
    """
    items = sorted(dataset, key=lambda x: x['price'], reverse=True)
    return items[:n]
```

This function sorts the `dataset` based on the `'price'` of the items in the dictionary. The `key` parameter in the `sorted` function is used to specify the key function to be applied to each item in the dataset. The `reverse` parameter is set to `True` to sort the items in descending order. Finally, the function returns a slice of the sorted items from index `0` to `n-1`.

For the given example, `expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)` would return `[{'name': 'Item-2', 'price': 555.22}]`.

"""

def expensive_items(dataset, n):
    """
    Find the n most expensive items in a given dataset.
    """
    items = sorted(dataset, key=lambda x: x['price'], reverse=True)
    return items[:n]

```