```
def sum_list(list1, list2):
    return [x+y for x,y in zip(list1, list2)]
```
This function uses the built-in `zip` function to pair up the corresponding elements of the two input lists. It then uses a list comprehension to add each pair of elements together and create a new list containing the results.

The unit test `assert sum_list([10,20,30],[15,25,35])==[25,45,65]` shows that the function should add the corresponding elements of the two input lists together to produce the output list. For example, `sum_list([10,20,30],[15,25,35])` should return `[25,45,65]`. The function will work for lists of any length, not just three elements. The `zip` function stops when the shorter list is exhausted, so if the lists are of different lengths, the extra elements in the longer list will be ignored. For example, `sum_list([1,2,3,4],[5,6,7])` would return `[6,8,9]`.