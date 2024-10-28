```
def incr_list(l: list):
    return [i + 1 for i in l]
```

This function takes a list of numbers as input and returns a new list where each element is incremented by 1. It uses a list comprehension to achieve this. The list comprehension iterates over each element `i` in the input list `l`, adds 1 to it, and includes the result in the new list. The new list is then returned by the function.

The unit tests provided ensure that the function works correctly for different input lists. For example, the first test case checks that the function correctly increments the list `[1, 2, 3]` to `[2, 3, 4]`. The second test case checks that the function correctly increments the list `[5, 3, 5, 2, 3, 3, 9, 0, 123]` to `[6, 4, 6, 3, 4, 4, 10, 1, 124]`. These tests help to ensure that the function is working correctly for different inputs.