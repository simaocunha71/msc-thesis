The task is to write a Python function that takes a list of elements as input and checks if all the elements in the list are unique. 

Here is a Python function that solves this problem:

```Python
def all_unique(lst):
    return len(lst) == len(set(lst))
```

This function works by comparing the length of the input list with the length of a set created from the list. In Python, a set is an unordered collection of unique elements. So, if the lengths are equal, it means that all elements in the list are unique. If the lengths are not equal, it means that there are duplicate elements in the list.

The unit test `assert all_unique([1,2,3]) == True` ensures that the function returns `True` when all elements in the list are unique.

Note: This function assumes that the input list is not empty. If the list can be empty, you may want to add a check at the beginning of the function to return `True` for an empty list, since an empty list is considered to have unique elements. For example:

```Python
def all_unique(lst):
    return len(lst) == len(set(lst)) or not lst
``` 