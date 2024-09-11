Here's one way you could do it:

```python
def expensive_items(dataset,n):
    return sorted(dataset,key=lambda d:d['price'],reverse=True)[:n]
```

This function works by sorting the dataset by the price of the items in descending order (i.e. from most to least expensive), and then returning a slice of that sorted list consisting of the first `n` items.

For example, if you call `expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)`, the function will return `[{'name': 'Item-2', 'price': 555.22}]` as expected.

Note that the function uses a `lambda` function as the `key` argument to the `sorted` function. This `lambda` function takes a dictionary `d` and returns the value of the 'price' key as the sorting criterion.
```

```
Here are some additional notes on the function:

- The function takes two arguments: `dataset`, which is the list of dictionaries representing the items, and `n`, which is the number of most expensive items you want to find.
- The function uses the `sorted` function to sort the `dataset` by the 'price' key in descending order. The `key` argument to the `sorted` function is a `lambda` function that takes a dictionary `d` and returns the value of the 'price' key. The `reverse` argument is set to `True` to sort the items in descending order.
- The `sorted` function returns a new list that is a sorted version of the `dataset`. The function then uses list slicing (`[:n]`) to return a slice of the sorted list consisting of the first `n` items, which are the most expensive items.

Overall, this function provides a simple and efficient way to find the `n` most expensive items in a given dataset.

```
```python
```
```
```
```
```
```
```
```
```
```python
```
```