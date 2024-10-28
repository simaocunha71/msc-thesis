```
def flatten_list(nested_list):
    result = []
    for element in nested_list:
        if type(element) == list:
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result
```


This function iterates over each element in the input list. If the element is itself a list, it recursively calls the function on that list and extends the result with the new list. If the element is not a list, it simply appends it to the result. The function continues until all elements are processed, resulting in a single, flat list. The unit test provided ensures that the function works correctly for a given input. 





