You can solve this problem by using the built-in set function in Python, which returns a set object containing the unique elements of the list. Then, you can compare the length of the set with the length of the list. If the lengths are equal, it means the list contains unique elements, otherwise, it means there are duplicate elements.

Here's a Python function that implements this:

```
def all_unique(lst):
    return len(lst) == len(set(lst))
```

This function works by converting the list to a set, which automatically removes any duplicate elements. It then compares the length of the original list with the length of the set. If the lengths are equal, it means the list contained no duplicate elements, so the function returns True. If the lengths are not equal, it means the list contained at least one duplicate element, so the function returns False.

The unit test `assert all_unique([1,2,3]) == True` ensures that the function returns True when the list contains unique elements. This test is passed because the function correctly identifies the list [1,2,3] as containing unique elements. 







