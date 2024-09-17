```
def add_lists(lst, tup):
    return tup + tuple(lst)
```



The task is to create a function that takes a list and a tuple as input, and returns a new tuple that is the result of appending the elements of the list to the tuple. For example, if the input list is [5, 6, 7] and the input tuple is (9, 10), the function should return the tuple (9, 10, 5, 6, 7).

The unit test `assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)` provides an example of how the function should behave.

Here is the solution:
```
def add_lists(lst, tup):
    return tup + tuple(lst)
```
This function uses the `+` operator to concatenate the tuple `tup` with the tuple created from the list `lst` using the `tuple()` function. The result is a new tuple that contains all the elements of the input tuple and list.