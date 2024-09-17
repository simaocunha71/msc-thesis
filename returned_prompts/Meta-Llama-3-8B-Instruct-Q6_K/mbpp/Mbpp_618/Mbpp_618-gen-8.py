```
def div_list(list1, list2):
    return [x / y for x, y in zip(list1, list2)]
```
The provided unit test `assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]` suggests that the division should be element-wise. The function `div_list` takes two lists as input, and returns a new list where each element is the result of the division of the corresponding elements in the input lists.

The `zip` function is used to iterate over the two input lists in parallel, and the division operation is performed using a list comprehension. This way, the function can handle lists of different lengths, as it will stop iterating when the shorter list is exhausted.

Note that this function assumes that the input lists are non-empty and that the second list is not empty at any point during the iteration. If this is not the case, the function may raise a ZeroDivisionError or produce incorrect results. You may want to add error handling or input validation to make the function more robust. 