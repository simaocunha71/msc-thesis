```
def expensive_items(dataset, n):
    sorted_dataset = sorted(dataset, key=lambda x: x['price'], reverse=True)
    return sorted_dataset[:n]
```



Explanation:
The function `expensive_items` takes a list of dictionaries `dataset` and an integer `n` as input. Each dictionary in `dataset` represents an item with a 'name' and a 'price'. The function returns a list of the n most expensive items in the dataset.

The function first sorts the dataset in descending order based on the 'price' of each item using the `sorted` function with a lambda function as the key. This means that the items with the highest prices will be at the beginning of the list.

Then, it returns a slice of the sorted list, from the beginning to the `n`th element. This slice contains the n most expensive items in the dataset.

For example, if the dataset is `[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}]` and `n` is 1, the function will return `[{'name': 'Item-2', 'price': 555.22}]`, which are the most expensive items in the dataset.