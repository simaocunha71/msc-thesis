You can use the following Python function to solve this problem:

```Python
def is_sublist(lst, sublst):
    if not isinstance(lst, list) or not isinstance(sublst, list):
        return False
    if not sublst:
        return True
    for i in range(len(lst)):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False
```
This function first checks if the input lists are valid. If the sublist is empty, it returns True. Then it iterates over the main list and checks if the sublist is present at each position. If the sublist is found, the function returns True. If the sublist is not found after checking all positions, the function returns False.

For example, `is_sublist([2,4,3,5,7],[3,7])` will return False because the sublist [3,7] is not present in the main list.  `is_sublist([2,4,3,5,7],[2,4])` will return True because the sublist [2,4] is present in the main list.  `is_sublist([2,4,3,5,7],[])` will return True because the empty sublist is considered to be a sublist of any list.  `is_sublist([], [1,2,3])` will return False because the main list is empty.  `is_sublist([], [])` will return True because the empty list is considered to be a sublist of the empty list.  `is_sublist([1,2,3], 1)` will return False because the second argument is not a list.  `is_sublist([1,2,3], 'abc')` will return False because the second argument is not a list.  `is_sublist([1,2,3], [1,2,3,4])` will return False because the sublist [1,2,3,4] is not present in the main list.  `is_sublist([1,2,3,4,3,2,1], [1,2,3])` will return True because the sublist [1,2,3] is present in the main list.  `is_sublist([1,2,3,4,5,6], [1,2,3,4,5,6])` will return True because the sublist [1,2,3,4