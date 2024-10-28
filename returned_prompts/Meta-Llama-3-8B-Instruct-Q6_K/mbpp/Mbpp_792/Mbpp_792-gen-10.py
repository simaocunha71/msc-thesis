```
def count_list(list_of_lists):
    return len(list_of_lists)
```
The function `count_list` takes a list of lists as an argument and returns the number of lists in the given list of lists. The unit test `assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4` ensures that the function works correctly. The function simply uses the built-in `len` function to count the number of elements in the list of lists, which is equivalent to the number of lists in the given list of lists. 