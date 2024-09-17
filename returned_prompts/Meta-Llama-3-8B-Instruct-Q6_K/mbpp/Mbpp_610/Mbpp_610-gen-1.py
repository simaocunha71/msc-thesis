```
def remove_kth_element(lst, k):
    lst.pop(k-1)
    return lst
```
This function uses the built-in list method pop() which removes the element at the specified position and returns it. The specified position is 0-indexed, so we subtract 1 from the input k. The function returns the modified list. 

For example, if we call remove_kth_element([1,1,2,3,4,4,5,1],3), it will remove the 3rd element (index 2) from the list and return the resulting list [1, 1, 3, 4, 4, 5, 1]. 

This function assumes that k is within the range of the list length. If k is out of range, it will raise an IndexError. If you want to handle this case, you can add a check at the beginning of the function. For example:
```
def remove_kth_element(lst, k):
    if k > len(lst):
        return lst  # or raise an exception, depending on your requirements
    lst.pop(k-1)
    return lst
``` 





