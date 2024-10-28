```
def expensive_items(data, n):
    return sorted(data, key=lambda x: x['price'], reverse=True)[:n]
```
This function takes a list of dictionaries `data` as input, where each dictionary represents an item with a 'name' and a 'price'. It also takes an integer `n` as input, which is the number of most expensive items to return.

The function uses the built-in `sorted` function to sort the items in the dataset by their prices in descending order. The `key` argument of the `sorted` function is a lambda function that extracts the 'price' from each dictionary. The `reverse=True` argument is used to sort in descending order.

The sorted list is then sliced to return the `n` most expensive items.

For example, if the input is `[{...}, {...}]` with `n=1`, the function will return the most expensive item. If the input is `[{...}, {...}, {...}]` with `n=2`, the function will return the two most expensive items, and so on.