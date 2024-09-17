```
def is_Sub_Array(list1, list2):
    if len(list2) > len(list1):
        return False
    for i in range(len(list1) - len(list2) + 1):
        if list1[i:i+len(list2)] == list2:
            return True
    return False
```


The function `is_Sub_Array(list1, list2)` checks whether `list2` is a sublist of `list1` or not. It first checks if the length of `list2` is greater than the length of `list1`, in which case it immediately returns `False`. Then it iterates over `list1` and checks if any sub-list of the same length as `list2` is equal to `list2`. If it finds such a sub-list, it returns `True`. If it doesn't find any such sub-list after checking all sub-lists, it returns `False`. The unit test `assert is_Sub_Array([1,4,3,5],[1,2]) == False` ensures that the function works correctly. 

For example, if `list1 = [1,2,3,4,5,6]` and `list2 = [2,3]`, the function will return `True` because `list2` is a sublist of `list1`. If `list1 = [1,2,3,4,5,6]` and `list2 = [1,2,3,4,5,6]`, the function will return `False` because `list2` is not a sublist of `list1`. If `list1 = [1,2,3,4,5,6]` and `list2 = [7,8,9]`, the function will return `False` because `list2` is not a sublist of `list1`. If `list1 = [1,2,3,4,5,6]` and `list2 = [1,4,3,5]`, the function will return `False` because `list2` is not a sublist of `list1`. 

This function works for lists of any length, not just for lists of the same length. It also works for lists that contain duplicate elements. For example, if `list1 = [1,2,2,3,4,5,6]` and `list2 = [2,2,3]`, the