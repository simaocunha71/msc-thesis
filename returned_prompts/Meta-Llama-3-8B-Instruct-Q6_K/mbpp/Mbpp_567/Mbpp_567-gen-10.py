```
def issort_list(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
```
This function takes a list as input and checks if it is sorted in ascending order. It iterates over the list, comparing each element with the next one. If it finds a pair of elements where the first is greater than the second, it immediately returns `False`, indicating that the list is not sorted. If it finishes the iteration without finding any such pair, it returns `True`, indicating that the list is sorted. 

The unit test `assert issort_list([1,2,4,6,8,10,12,14,16,17])==True` suggests that the list is sorted, so this function should return `True` for this input.  If the list were not sorted, the function would return `False`. 

Note that this function assumes that the list is non-empty and that the elements are comparable (i.e., they can be compared using the `>` operator). If the list is empty or contains non-comparable elements, this function may not work correctly.  It also assumes that the list is sorted in ascending order; if it is sorted in descending order, this function will incorrectly report that the list is not sorted.  If you need to check for these cases or for sorting in descending order, you would need to modify the function accordingly.  For example, you could add checks for an empty list or for non-comparable elements, or you could modify the comparison in the loop to use the `<` operator instead of `>`.  You could also add a second function that checks for sorting in descending order, or a function that checks for sorting in either ascending or descending order.  The possibilities are endless!  But for now, this function should work correctly for the specific case where the list is non-empty, contains comparable elements, and is sorted in ascending order.  Happy coding!  😊
```python
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
``` 
This unit test checks if the function `issort_list` returns `True` for the input list `[1,2,4,6,8,10,12,14,16,17]`. If the function returns `True`, the test passes; if it returns anything else, the test fails.