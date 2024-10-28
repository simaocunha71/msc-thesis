```
def incr_list(l: list):
    return [x+1 for x in l]
```


This function takes a list of integers as input and returns a new list where each element is incremented by 1. The function uses a list comprehension to create the new list. It iterates over each element in the input list, adds 1 to it, and adds the result to the new list. The input list is not modified. For example, `incr_list([1, 2, 3])` returns `[2, 3, 4]`. The function is tested using the provided unit tests. The unit tests check that the function returns the expected result for the provided input lists. The unit tests are:
```
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The unit tests can be run in a Python interpreter or using a testing framework like unittest. The function is correct and works as expected. It is also efficient, as it uses a list comprehension to create the new list, which is faster than using a for loop.