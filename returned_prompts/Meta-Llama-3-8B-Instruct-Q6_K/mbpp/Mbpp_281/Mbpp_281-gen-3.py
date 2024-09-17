```
def all_unique(lst):
    return len(lst) == len(set(lst))
```
This function works by comparing the length of the original list to the length of a set created from the list. In Python, a set is an unordered collection of unique elements. If the lengths are equal, it means that all elements in the list are unique. If the lengths are not equal, it means that there are duplicate elements in the list.

For example, if you call `all_unique([1,2,3])`, the function will return `True` because the lengths of the lists are equal. If you call `all_unique([1,2,2])`, the function will return `False` because the lengths of the lists are not equal. The set created from the list `[1,2,2]` will be `{1,2}`, which has only two elements, so the function will return `False`.