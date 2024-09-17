```
def max_length(list_of_lists):
    max_length = 0
    max_list = []
    for lst in list_of_lists:
        if len(lst) > max_length:
            max_length = len(lst)
            max_list = lst
    return max_length, max_list
```
This function iterates over each list in the list of lists. If the length of the current list is greater than the current maximum length, it updates the maximum length and the corresponding list. Finally, it returns the maximum length and the corresponding list. The unit test `assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])` ensures that the function works correctly.