Here's one way to do it:

```python
def expensive_items(dataset,n):
    items = sorted(dataset, key=lambda x: x['price'], reverse=True)[:n]
    return items
```

This function first sorts the dataset by price in decreasing order. Then it slices the first n items from the sorted list.

The key here is the `sorted` function which can accept a `key` argument to determine the sorting order. In this case, we're sorting by the 'price' attribute of each item.

The `lambda x: x['price']` part is a function that takes an item and returns its 'price' attribute. This function is used as the `key` argument to the `sorted` function, meaning that the items will be sorted based on their 'price' attribute.

Finally, `[:n]` is used to slice the first `n` items from the sorted list.

To test the function, you can use the `assert` statement to check if the function returns the expected result for a given dataset and `n`.

```python
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
```

This will raise an `AssertionError` if the function doesn't return the expected result.

Note: This implementation assumes that the dataset is a list of dictionaries, where each dictionary represents an item and has 'name' and 'price' attributes.

"""
```python
def expensive_items(dataset,n):
    items = sorted(dataset, key=lambda x: x['price'], reverse=True)[:n]
    return items
```

This function first sorts the dataset by price in decreasing order. Then it slices the first n items from the sorted list.

The key here is the `sorted` function which can accept a `key` argument to determine the sorting order. In this case, we're sorting by the 'price' attribute of each item.

The `lambda x: x['price']