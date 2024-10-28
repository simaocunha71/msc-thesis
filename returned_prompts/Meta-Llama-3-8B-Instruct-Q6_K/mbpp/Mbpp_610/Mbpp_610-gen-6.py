```
def remove_kth_element(lst, k):
    lst.pop(k-1)
    return lst
```


The unit test `assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]` suggests that the function should remove the k'th element from the list and return the remaining elements. The `pop` method of a list is used to remove the element at the specified position. The position is specified by the index, which is `k-1` because list indices start at 0. The function returns the modified list.

However, it's important to note that this function does not handle the case where k is larger than the length of the list. It also does not handle the case where k is less than 1. Depending on the requirements of the problem, the function may need to be modified to handle these cases. For example, it could raise an exception if k is out of range, or it could return the original list if k is less than 1. 

Here is a modified version of the function that raises an exception if k is out of range:

```
def remove_kth_element(lst, k):
    if k < 1 or k > len(lst):
        raise ValueError("k is out of range")
    lst.pop(k-1)
    return lst
```

And here is a modified version that returns the original list if k is less than 1:

```
def remove_kth_element(lst, k):
    if k < 1:
        return lst
    lst.pop(k-1)
    return lst
```


And here is a modified version that returns the original list if k is larger than the length of the list:

```
def remove_kth_element(lst, k):
    if k > len(lst):
        return lst
    lst.pop(k-1)
    return lst
```


You can choose the behavior that best fits your requirements. 