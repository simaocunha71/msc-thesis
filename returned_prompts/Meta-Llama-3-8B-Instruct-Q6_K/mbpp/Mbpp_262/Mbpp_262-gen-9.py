```
def split_two_parts(lst, L):
    return (lst[:L], lst[L:])
```


In this function, we use Python's list slicing feature to create two lists. The first list (`lst[:L]`) contains the first L elements of the input list, and the second list (`lst[L:]`) contains the remaining elements. The function returns these two lists as a tuple. This solution passes the given unit test. 
However, please note that this function does not handle the case where the length of the input list is less than L. It will simply truncate the list if it is shorter than L. If you want to handle this case differently, you would need to add additional logic to the function.  For example, you might want to return the original list if it is shorter than L, or raise an exception if L is larger than the length of the list.  The exact behavior will depend on your specific requirements. 
```python
def split_two_parts(lst, L):
    if L > len(lst):
        return (lst, [])
    return (lst[:L], lst[L:])
``` 
This version of the function checks if L is larger than the length of the list, and if so, returns a tuple where the first element is the original list and the second element is an empty list. This handles the case where L is larger than the length of the list. 
```python
def split_two_parts(lst, L):
    if L > len(lst):
        raise ValueError("L is larger than the length of the list")
    return (lst[:L], lst[L:])
``` 
This version of the function raises a ValueError if L is larger than the length of the list. This will cause the function to stop execution and raise an error if L is larger than the length of the list. You could also return a different value, such as None or a special value, depending on your specific requirements.  The exact behavior will depend on your specific requirements. 
```python
def split_two_parts(lst, L):
    if L < 0:
        raise ValueError("L must be a non-negative integer")
    return (lst[:L], lst[L:])
``` 
This version of the function raises a ValueError if L is less than 0. This will cause the function to stop execution and raise an error if L is less than 0. You could also return a different value, such as None or a special value, depending on your specific requirements.  The exact behavior will depend