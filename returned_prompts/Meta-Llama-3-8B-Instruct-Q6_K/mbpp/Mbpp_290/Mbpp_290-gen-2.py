You can solve this problem by using a list comprehension to get the lengths of all the lists and then use the max function to find the maximum length. Then, use another list comprehension to get the list with the maximum length.

Here is the Python code for the above solution:

```
def max_length(list_of_lists):
    max_len = max(len(sublist) for sublist in list_of_lists)
    max_sublist = [sublist for sublist in list_of_lists if len(sublist) == max_len][0]
    return max_len, max_sublist
```

This function takes a list of lists as input, finds the maximum length of the lists, and then returns the maximum length and the list with the maximum length. 

For example, if you call `max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])`, it will return `(3, [13, 15, 17])` because `[13, 15, 17]` is the list with the maximum length 3. 

This function will work correctly even if there are multiple lists with the maximum length. It will return the first list it encounters with the maximum length. If you want to return all lists with the maximum length, you would need to modify the function to return a list of lists instead of a single list. 

The unit test `assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])` ensures that the function works correctly for this specific input. 

Note that this function assumes that the input list is not empty. If the input list could be empty, you should add a check for this case and return a suitable value (e.g., `(0, [])` or `None`). 

Also, this function does not handle the case where there are multiple lists with the same maximum length. If you want to handle this case, you would need to modify the function to return a list of lists or a dictionary mapping lengths to lists. 