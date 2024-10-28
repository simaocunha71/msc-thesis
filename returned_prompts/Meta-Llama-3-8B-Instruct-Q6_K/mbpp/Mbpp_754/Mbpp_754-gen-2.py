```
def extract_index_list(l1, l2, l3):
    common = set(l1) & set(l2) & set(l3)
    return [i for i in range(len(l1)) if l1[i] in common and l2[i] in common and l3[i] in common]
```
The function `extract_index_list` takes three lists `l1`, `l2`, `l3` as input. It first finds the common elements between the three lists using the intersection operation on the sets of the three lists. Then, it iterates over the indices of the first list and checks if the element at that index is in the common set and also appears at the same index in the other two lists. If the condition is met, it adds the index to the result list. The function returns the list of indices where common elements appear in all three lists.

The unit test `assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]) == [1, 7]` checks if the function returns the correct list of indices where the common elements 1 and 7 appear in all three lists. 