```
def unique_Element(lst):
    return len(set(lst)) == 1
```


The function `unique_Element(lst)` takes a list `lst` as input and returns `True` if the list contains only one distinct element, and `False` otherwise.

The function uses the `set` data structure to remove duplicate elements from the list. If the length of the set is equal to 1, it means that the list contains only one distinct element, and the function returns `True`. Otherwise, it returns `False`.

The unit test `assert unique_Element([1,1,1]) == True` ensures that the function returns `True` when the list contains only one distinct element. This test case is based on the given problem statement, which does not specify that the list should contain only one distinct element that is not equal to any other element. However, the unit test clarifies this assumption and ensures that the function behaves correctly in this scenario.