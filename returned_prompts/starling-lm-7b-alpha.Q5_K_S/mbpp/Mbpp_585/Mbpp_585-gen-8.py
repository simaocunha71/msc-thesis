Here is one possible solution:

```python
def expensive_items(dataset,n):
    # Sort the dataset by price in descending order.
    dataset.sort(key = lambda x: x['price'], reverse=True)
    return dataset[:n]
```

This function will return the first n items of the sorted dataset, which are the most expensive ones.

```python
# Test case
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
```

In this test case, the dataset only has 2 items, and we want to find the most expensive item. After sorting the dataset by price in descending order, the first item is the most expensive one, so the function returns `[{'name': 'Item-2', 'price': 555.22}]`.

```python
# Test case
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22},{'name': 'Item-3', 'price': 222.22},{'name': 'Item-4', 'price': 131.13}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-3', 'price': 222.22}]
```

In this test case, the dataset has 4 items, and we want to find the 2 most expensive items. After sorting the dataset by price in descending order, the first two items are the most expensive ones, so the function returns `[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-3', 'price': 222.22}]`.

```python
# Test case
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 55