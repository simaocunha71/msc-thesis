The problem is asking to create a function that checks if all elements in a given list are unique or not. 
The function should return True if all elements are unique and False otherwise.

Here's a Python function that accomplishes this:

```
def all_unique(lst):
    return len(lst) == len(set(lst))
```

This function works by comparing the length of the original list with the length of a set created from the list. 
In Python, a set is an unordered collection of unique elements. 
So, if the lengths are equal, it means all elements in the list are unique. 
If the lengths are not equal, it means there are duplicate elements in the list.

The unit test `assert all_unique([1,2,3]) == True` ensures that the function returns True for a list with unique elements. 

For example, if you call `all_unique([1,2,3])`, the function will return True because all elements in the list are unique. 
If you call `all_unique([1,2,2])`, the function will return False because there are duplicate elements in the list. 