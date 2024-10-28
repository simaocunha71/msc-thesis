```
def Extract(lst):
    return [sublist[0] for sublist in lst]
```


Here's an explanation of the solution:

*   The problem asks to write a function that takes a list of sublists as input and returns a new list containing the first element of each sublist.
*   The unit test `assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]` helps to clarify the expected output.
*   The solution uses a list comprehension to iterate over the input list of sublists and extract the first element of each sublist.
*   The `sublist[0]` expression retrieves the first element of each sublist, and the list comprehension `[... for sublist in lst]` collects these elements into a new list.
*   The resulting list is returned by the function. In this case, `Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]])` would return the list `[1, 3, 6]`.