```
def unique_sublists(lists):
    result = {}
    for item in lists:
        if isinstance(item, list):
            item = tuple(sorted(item))
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
```    
    This function iterates over the list of lists. If an item is a list, it converts it to a tuple and sorts it. Then it checks if this tuple is already in the result dictionary. If it is, it increments the count by 1. If not, it adds the tuple to the dictionary with a count of 1. The function returns the dictionary.

The unit test `assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}` ensures that the function works correctly. It checks if the output of the function is equal to the expected output.

This function assumes that the input list only contains lists or non-list elements. It does not handle cases where the input list contains other types of elements. It also assumes that the input list is not empty. If the input list is empty, the function will return an empty dictionary. 