```
def flatten_list(nested_list):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result
```
The function `flatten_list` takes a nested list as input and returns a flattened list. It iterates over each element in the input list. If the element is a list itself, it recursively calls `flatten_list` on that sublist and extends the result list with the flattened sublist. If the element is not a list, it simply appends the element to the result list. The function returns the flattened list. The unit test `assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]` checks that the function correctly flattens the given nested list. 