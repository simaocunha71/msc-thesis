The task is to write a function that takes a nested list structure as input and returns a flattened list. This means that all the sublists within the main list should be removed, leaving only the individual elements.

Here is a Python solution for this problem:
```
def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if type(element) == list:
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list
```
This function works by iterating over each element in the input list. If the element is itself a list, the function calls itself with that list as the input, effectively flattening it. The results of these recursive calls are then added to the main list using the extend method. If the element is not a list, it is simply added to the main list using the append method.

The unit test `assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]` ensures that the function works correctly for this specific input. It checks that the output of the function is equal to the expected result. If the function is correct, this test will pass; if the function is incorrect, this test will fail.