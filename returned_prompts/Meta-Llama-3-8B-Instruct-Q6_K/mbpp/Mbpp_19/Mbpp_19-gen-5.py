```
def has_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
```


The function `has_duplicates` takes a list of integers as input and returns `True` if the list contains any duplicate elements and `False` otherwise.

The function works by iterating over the list and adding each element to a set. If an element is already in the set, it means that the list contains a duplicate and the function returns `True`. If the function finishes iterating over the list without finding any duplicates, it returns `False`.

The unit test `assert test_duplicate(([1,2,3,4,5]))==False` checks that the function returns `False` for a list that does not contain any duplicates. This test helps to ensure that the function is working correctly. 







