```
def consecutive_duplicates(lst):
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            result.append(lst[i])
    return result
```


This function iterates over the list, checking if each element is different from the previous one. If it is, it is added to the result list. The result list is then returned. The unit test provided ensures that the function works correctly, removing consecutive duplicates while preserving the original order of elements. 
For example, the unit test `assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]` ensures that the function correctly removes consecutive duplicates from the input list. 