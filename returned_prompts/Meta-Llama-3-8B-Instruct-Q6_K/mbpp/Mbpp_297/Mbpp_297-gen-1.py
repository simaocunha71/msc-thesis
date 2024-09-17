The problem is asking to create a function that takes a nested list as input and returns a new list with all the nested lists flattened. 

Here's a Python solution using recursion:

```
def flatten_list(nested_list):
    flattened_list = []
    for element in nested_list:
        if isinstance(element, list):
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    return flattened_list
```

This function works by iterating over each element in the input list. If the element is itself a list, the function calls itself with that list as the input, effectively flattening it. If the element is not a list, it is simply appended to the result list. The `extend` method is used to add all the elements of the flattened list to the result list, rather than just appending the list itself. 

The unit test provided ensures that the function works correctly for the given input. It checks that the output of the function is the expected list when given the specified input. 

For example, the test case `assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]` ensures that the function correctly flattens the input list. 

This solution assumes that the input list is well-formed, i.e., it does not contain any non-list elements that are not instances of the `list` type. If the input list can contain such elements, additional error handling would be needed. 