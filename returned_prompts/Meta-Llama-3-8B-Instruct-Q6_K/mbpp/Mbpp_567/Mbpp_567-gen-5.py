```
def issort_list(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
```


The function `issort_list` takes a list as input and returns `True` if the list is sorted in ascending order, and `False` otherwise. It does this by iterating over the list and comparing each element to the next one. If it finds a pair of elements where the first is greater than the second, it immediately returns `False`. If it gets through the entire list without finding such a pair, it returns `True`, indicating that the list is sorted. This function is based on the definition of a sorted list, which is a list where each element is less than or equal to the next one. The unit test `assert issort_list([1,2,4,6,8,10,12,14,16,17])==True` ensures that the function correctly identifies a list as sorted.