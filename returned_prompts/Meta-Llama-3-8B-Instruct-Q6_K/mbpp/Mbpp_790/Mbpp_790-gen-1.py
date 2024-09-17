```
def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True
```


The function iterates over the list with a step size of 2, starting from the first element (index 0). For each even-indexed element, it checks if the element is even by using the modulus operator `%`. If it finds an element that is not even, it immediately returns `False`. If it checks all even-indexed elements and doesn't find any that are not even, it returns `True`. The unit test `assert even_position([3,2,1]) == False` ensures that the function works correctly.  The function passes this test, so it is correct. 
However, this function will not work correctly if the list is empty. It would be better to add a check at the beginning of the function to return `True` for an empty list, since an empty list does not contain any even-indexed elements. Here's how you could modify the function to include this check:

```
def even_position(lst):
    if len(lst) == 0:
        return True
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True
```  This version of the function will return `True` for an empty list, and it will still return `False` if it finds an even-indexed element that is not even. It will also still return `True` if it checks all even-indexed elements and doesn't find any that are not even.  This version of the function passes the unit test `assert even_position([3,2,1]) == False`, and it will also return `True` for an empty list, as expected.  Therefore, this function is correct and can be used to solve the problem. 