```
def expensive_items(dataset, n):
    return sorted(dataset, key=lambda x: x['price'], reverse=True)[:n]
```
This function sorts the dataset in descending order based on the price of each item and then returns the n most expensive items. The `sorted` function is used with a lambda function as the key to specify the sorting criterion. The `reverse=True` argument is used to sort in descending order. The `[:n]` slicing is used to return the n most expensive items.

For example, if the dataset is `[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}]` and n is 1, the function will return `[{'name': 'Item-2', 'price': 555.22}]`, which are the most expensive items in the dataset. 

The unit test `assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]` passes, confirming that the function works correctly. 