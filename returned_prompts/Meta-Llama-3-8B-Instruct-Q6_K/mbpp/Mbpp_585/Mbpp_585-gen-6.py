```
def expensive_items(data, n):
    data.sort(key=lambda x: x['price'], reverse=True)
    return data[:n]
```


The function `expensive_items` takes two parameters: a list of dictionaries `data` and an integer `n`. Each dictionary in the list represents an item with a 'name' and a 'price'. The function sorts the list of dictionaries in descending order based on the 'price' of each item and then returns the first `n` items in the sorted list.

The unit test `assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]` ensures that the function returns the most expensive item when `n` is 1.