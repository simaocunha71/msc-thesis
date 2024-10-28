```
def sum_list(a, b):
    return [i + j for i, j in zip(a, b)]
```


This function uses Python's built-in list comprehension and the zip function to add corresponding elements from the two input lists. The zip function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The list comprehension then adds each pair of elements and returns the result as a list. 

For example, if we call `sum_list([10,20,30], [15,25,35])`, it will return the list `[25, 45, 65]`, which is the result of adding corresponding elements from the two input lists. 

The unit test `assert sum_list([10,20,30],[15,25,35])==[25,45,65]` ensures that the function works correctly. 

Note that this function assumes that the two input lists have the same length. If the lists have different lengths, the function will stop at the end of the shorter list and ignore any extra elements in the longer list. If you need to handle lists of different lengths, you may need to add additional error checking or padding. 