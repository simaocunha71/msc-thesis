```
def is_sublist(lst, sublst):
    if not isinstance(lst, list) or not isinstance(sublst, list):
        return False
    if len(sublst) > len(lst):
        return False
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False
```


The function `is_sublist` checks if a given list contains a sublist. It first checks if the input is a list and if the sublist is not longer than the main list. Then it iterates over the main list and checks for each position if the sublist matches. If a match is found, it returns `True`. If no match is found after checking all positions, it returns `False`. The function is tested with the given unit test `assert is_sublist([2,4,3,5,7],[3,7])==False`. This test fails because the function is not correctly implemented. The function should return `False` in this case because the sublist `[3,7]` is not in the list `[2,4,3,5,7]`. The correct implementation of the function is provided above. This function correctly identifies whether a list contains a sublist or not. 





