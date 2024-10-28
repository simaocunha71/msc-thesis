```
def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
```



The provided unit test is:
```
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
```



The function `flatten_list` takes a nested list as input and returns a flat list. It iterates over each item in the input list. If the item is a list itself, the function calls itself recursively with the item as the input, effectively flattening the sublist. If the item is not a list, it is simply appended to the flat list. The flattened list is then returned. The unit test provided checks if the function works correctly for a given input. 














The problem is asking to create a function that takes a nested list as an input and returns a flat list. The function should be able to handle lists of varying depths.

The unit test provided is:
```
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
```

The solution to this problem is a recursive function that checks if each element in the input list is a list itself. If it is, the function calls itself with the sublist as the input, effectively flattening the sublist. If the element is not a list, it is simply appended to the flat list.

Here is the solution:
```
def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
```

This function works by iterating over each element in the input list. If the element is a list, the function calls itself with the sublist as the input,