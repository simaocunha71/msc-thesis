```
def issort_list(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```





Python's built-in function `all()` returns `True` if all elements of the iterable (in this case, a generator expression) are true. The generator expression checks if each element in the list is less than or equal to the next element. If any element is not less than or equal to the next, the function returns `False`, indicating that the list is not sorted. If the list is sorted, the function returns `True`. The unit test `assert issort_list([1,2,4,6,8,10,12,14,16,17])==True` confirms that the function correctly identifies a sorted list.