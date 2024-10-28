```
def Find_Min(lst):
    min_len = float('inf')
    min_sublist = []
    for sublist in lst:
        if len(sublist) < min_len:
            min_len = len(sublist)
            min_sublist = sublist
    return min_sublist
```
The function Find_Min takes a list of lists (sublists) as input and returns the sublist with the minimum length. It iterates over each sublist in the list, checks if the length of the current sublist is less than the minimum length found so far, and updates the minimum length and the minimum sublist if necessary. Finally, it returns the minimum sublist.

The unit test `assert Find_Min([[1],[1,2],[1,2,3]]) == [1]` ensures that the function works correctly by checking that the function returns the sublist `[1]` which has the minimum length among the sublists `[[1],[1,2],[1,2,3]]`.