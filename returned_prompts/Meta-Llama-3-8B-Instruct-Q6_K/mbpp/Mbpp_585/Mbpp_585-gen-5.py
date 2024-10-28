```
def expensive_items(data, n):
    expensive = sorted(data, key=lambda x: x['price'], reverse=True)[:n]
    return [item for item in expensive]
```
This function takes in a list of dictionaries, where each dictionary represents an item with a 'name' and a 'price'. It then sorts the list in descending order based on the 'price' and returns the top n items. If n is larger than the number of items in the dataset, it will return all items.

The unit test provided ensures that the function works correctly. It creates a list of two items, sorts them by price in descending order, and then returns the most expensive item when n is 1. The output should be [{'name': 'Item-2', 'price': 555.22}] as expected. 