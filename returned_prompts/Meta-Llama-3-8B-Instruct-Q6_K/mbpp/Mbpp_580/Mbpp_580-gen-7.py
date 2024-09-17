```
def extract_even(nested_tuple):
    result = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            result.append(extract_even(element))
        elif element % 2 == 0:
            result.append(element)
    return tuple(result)
```
This function uses recursion to traverse the nested tuple. It checks each element to see if it's a tuple, in which case it calls itself with that tuple as the argument. If the element is not a tuple, it checks if it's even and if so, adds it to the result list. Finally, it returns the result list as a tuple. The unit test provided ensures that the function works correctly for the given example.