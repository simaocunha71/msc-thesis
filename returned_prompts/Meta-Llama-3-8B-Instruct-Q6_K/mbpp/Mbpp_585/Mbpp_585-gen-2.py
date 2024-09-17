```
def expensive_items(dataset, n):
    return sorted(dataset, key=lambda x: x['price'], reverse=True)[:n]
```


This function sorts the dataset in descending order based on the price of each item, and then returns the first n items. 

The unit test `assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]` ensures that the function works correctly. 

For example, if the dataset is `dataset = [{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}]` and `n = 1`, the function should return ` [{'name': 'Item-2', 'price': 555.22}]`. 

The function works by first sorting the dataset based on the price of each item in descending order. This is done using the `sorted` function and a lambda function as the `key` argument. The `reverse=True` argument is used to sort the dataset in descending order. 

Then, the function returns the first `n` items of the sorted dataset using slicing. The `[:]` operator is used to return a slice of the sorted dataset. The slice starts from the beginning of the dataset and ends at the `n`th item. 

This function assumes that the dataset is a list of dictionaries, where each dictionary represents an item with a 'name' and a 'price'. The function also assumes that the 'price' values are numbers. If the 'price' values are not numbers, the function may not work correctly. 

The time complexity of this function is O(n log n) because it uses the `sorted` function, which has a time complexity of O(n log n) for sorting a list of n items. The space complexity of this function is O(n) because it returns a new list of the n most expensive items. 
```python
dataset = [{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}]
n = 1
print(expensive_items(dataset, n))  # Output: [{'name': 'Item-2', 'price': 555.22}]
```  ```python
dataset = [{'name': 'Item-1