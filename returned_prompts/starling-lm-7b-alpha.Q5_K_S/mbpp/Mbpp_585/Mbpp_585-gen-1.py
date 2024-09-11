```
def expensive_items(dataset, n):
    items = sorted(dataset, key=lambda item: item['price'], reverse=True)[:n]
    return [item for item in items]
```

Explanation:
The function `expensive_items` takes two parameters: `dataset`, which is a list of dictionaries, and `n`, which is the number of most expensive items to return. 

Inside the function, the `sorted` function is used to sort the `dataset` based on the `'price'` key in each dictionary. The `key` parameter is set to a lambda function that extracts the `'price'` value from each dictionary. The `reverse` parameter is set to `True` to sort the items in descending order. 

The `[:n]` syntax is used to slice the sorted `dataset` and keep only the first `n` items. 

Finally, a list comprehension is used to create a new list with the `n` most expensive items, and this list is returned as the result.

The given assertion checks if the function correctly returns the `n` most expensive items when given a sample dataset and `n` value.

This solution should correctly find the `n` most expensive items in a given dataset.

```python
expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)
```

This code will return `[{'name': 'Item-2', 'price': 555.22}]`, which is the most expensive item in the dataset.

```python
expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22},{'name': 'Item-3', 'price': 100.00}], 2)
```

This code will return `[{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 100.00}]`, which are the two most expensive items in the dataset.