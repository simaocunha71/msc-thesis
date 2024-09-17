```
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i]%2 != 0:
            return False
    return True
```


The function `even_position` takes a list `lst` as an argument. It iterates over the list with a step of 2, meaning it checks every even index. If it finds an index where the number is not even (i.e., `lst[i]%2 != 0`), it immediately returns `False`. If it checks all even indices and finds no numbers that are not even, it returns `True`. 

The unit test `assert even_position([3,2,1]) == False` helps to clarify the problem. It shows that the function should return `False` when there is at least one number at an even index that is not even. 

This function assumes that the input list is not empty. If the list can be empty, you should add a check at the beginning of the function to handle this case. For example, you could return `True` for an empty list, since there are no even indices to check.  Here is the modified function:

```
def even_position(lst):
    if not lst:
        return True
    for i in range(0, len(lst), 2):
        if lst[i]%2 != 0:
            return False
    return True
```


This function will return `True` for an empty list, and it will still work correctly for lists that are not empty.  It will return `False` if it finds a number at an even index that is not even, and it will return `True` if it checks all even indices and finds no numbers that are not even.  This function meets the requirements of the problem and passes the given unit test. 