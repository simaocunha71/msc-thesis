```
def flatten_list(nested_list):
    flattened_list = []
    for element in nested_list:
        if type(element) == list:
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    return flattened_list
```



In this solution, we define a function `flatten_list` that takes a nested list as input and returns a flattened list. We iterate over each element in the input list. If the element is a list itself, we recursively call `flatten_list` on it and extend the result to the `flattened_list`. If the element is not a list, we simply append it to the `flattened_list`. The function returns the flattened list.

The unit test `assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]` ensures that the function works correctly for a given example. It checks if the output of the function is equal to the expected result. If they are equal, the test passes; otherwise, it fails.