Here is a Python solution for the problem:

```Python
def isSorted(lst):
    if len(lst) < 2:
        return True
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
        elif lst[i] == lst[i-1]:
            return False
    return True
```
The function `isSorted` checks if a list of integers is sorted in ascending order. If the list has less than two elements, it returns `True` because a list with one or zero elements is considered sorted. It then iterates over the list, checking each element against the previous one. If it finds a pair of elements where the second element is less than the first, or if it finds a pair of equal elements, it returns `False` because the list is not sorted. If it finishes the loop without finding any such pairs, it returns `True` because the list is sorted. 

The function also handles the case where the list has more than one duplicate of the same number by returning `False` as soon as it finds a duplicate. This is because the problem statement specifies that the list should have no more than one duplicate of the same number. 

You can test the function with the examples provided in the problem statement. For example, `isSorted([5])` should return `True`, `isSorted([1, 2, 3, 4, 5])` should return `True`, and `isSorted([1, 3, 2, 4, 5])` should return `False`. 