```
def unique_sublists(lst):
    sublists = [tuple(sublist) for sublist in lst]
    unique_sublists = set(sublists)
    result = {}
    for sublist in unique_sublists:
        result[sublist] = sublists.count(sublist)
    return result
```


This function first converts all the lists in the input list into tuples. Then it converts this list of tuples into a set, which automatically removes any duplicate tuples. Finally, it iterates over this set, counting the number of occurrences of each tuple in the original list and stores these counts in a dictionary. The function returns this dictionary.

The unit test `assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}` helps to ensure the function is working correctly. It checks that the function returns the expected dictionary for the given input list. If the function is working correctly, the assertion will pass; otherwise, it will raise an AssertionError. 