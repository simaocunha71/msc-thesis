```
def combinations_list(lst):
    if not lst:
        return [ [] ]
    result = []
    for i, item in enumerate(lst):
        for combination in combinations_list(lst[:i] + lst[i+1:]):
            result.append([item] + combination)
    return result
```


The function `combinations_list` generates all possible combinations of the elements in the given list. It does this by recursively calling itself with the list minus the current item, and then prepending the current item to each combination. If the list is empty, it returns a list containing an empty list. This is because there is one combination of an empty list: the empty list itself. The function then combines all these combinations to get the final result. The unit test provided checks that this function works correctly.