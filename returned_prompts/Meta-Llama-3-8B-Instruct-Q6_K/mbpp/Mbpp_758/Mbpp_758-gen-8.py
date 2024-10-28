```
def unique_sublists(lst):
    result = {}
    for sublst in lst:
        sublst = tuple(sublst)
        if sublst in result:
            result[sublst] += 1
        else:
            result[sublst] = 1
    return result
```


This function iterates over the list of lists and for each sublist, it converts it to a tuple. If the tuple is already in the result dictionary, it increments the count; otherwise, it adds the tuple with a count of 1. The function returns the result dictionary.

The unit test `assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}` ensures that the function correctly counts the occurrences of each sublist.