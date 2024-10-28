```
def is_sorted(lst):
    if len(lst) <= 1:
        return True
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
        elif lst[i] == lst[i-1]:
            return False
    return True
```


The function `is_sorted` takes a list of integers as input and returns a boolean indicating whether the list is sorted in ascending order. If the list has more than one duplicate of the same number, the function returns `False`. 

The function first checks if the list has only one or zero elements, in which case it returns `True` as a single-element list is considered sorted. 

Then it iterates over the list starting from the second element (index 1). For each element, it checks if it is less than the previous element. If it is, the function returns `False` as the list is not sorted. 

If the current element is equal to the previous element, the function also returns `False` as the list has duplicate elements. 

If the function finishes iterating over the list without finding any elements that are less than or equal to the previous element, or any duplicate elements, it returns `True`, indicating that the list is sorted. 

This function assumes that the input list contains only positive integers and that there are no negative numbers. It also assumes that the list is not empty. 

The function can be tested with the provided examples to ensure it works correctly. 