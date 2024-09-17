```
def issort_list(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
This function uses the built-in `all()` function in Python, which returns `True` if all elements of the iterable (in this case, a generator expression) are true. The generator expression `lst[i] <= lst[i+1] for i in range(len(lst)-1)` checks if each element in the list is less than or equal to the next element. If all elements pass this test, the function returns `True`, indicating that the list is sorted. If any element fails this test, the function returns `False`, indicating that the list is not sorted. 

For example, the unit test `assert issort_list([1,2,4,6,8,10,12,14,16,17])==True` checks if the list is sorted and returns `True` as expected. 

Note that this function assumes that the list is either sorted in ascending or descending order. If the list can be sorted in either order, you would need to add additional logic to handle this.  Also, this function does not handle the case where the list is empty, which could be considered a special case.  It's always a good idea to add error checking code to handle such edge cases.  For example, you could add a check at the beginning of the function to return `True` if the list is empty, since an empty list is considered sorted.  Here is how you could modify the function to include this check:

```
def issort_list(lst):
    if len(lst) == 0:
        return True
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
This version of the function will return `True` if the list is empty, and will still correctly check if the list is sorted if it is not empty.  You could also add a check for the case where the list has only one element, since a list with only one element is also considered sorted.  Here is how you could modify the function to include this check:

```
def issort_list(lst):
    if len(lst) < 2:
        return True
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
This version of the function will return `True` if the list has one or zero elements, and will still correctly