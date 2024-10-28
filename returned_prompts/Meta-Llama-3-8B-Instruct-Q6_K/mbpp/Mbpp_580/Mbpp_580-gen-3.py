```
def extract_even(nested_tuple):
    result = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            result.append(tuple(filter(lambda x: x % 2 == 0, element)))
        elif element % 2 == 0:
            result.append(element)
    return tuple(result)
```


This function works by iterating over each element in the input tuple. If the element is a tuple itself, it uses the `filter` function to remove all odd numbers from the tuple, and then converts the result back to a tuple. If the element is not a tuple (i.e., it's a single number), it checks if the number is even, and if so, adds it to the result. Finally, it returns the result as a tuple. The unit test provided ensures that the function works correctly for the given example.