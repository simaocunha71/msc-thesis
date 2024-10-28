```
def unique(l: list):
    return sorted(set(l))
```


This function takes a list as input and returns a sorted list of unique elements. It does this by converting the list to a set, which automatically removes any duplicate elements, and then converting the set back to a list and sorting it.

The unit test provided in the problem statement ensures that the function works correctly. The test case checks that the function returns the sorted unique elements in the list `[5, 3, 5, 2, 3, 3, 9, 0, 123]`. The expected output is `[0, 2, 3, 5, 9, 123]`, which is the correct sorted unique elements in the list.