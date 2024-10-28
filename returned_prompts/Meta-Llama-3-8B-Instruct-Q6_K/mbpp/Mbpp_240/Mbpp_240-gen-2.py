```
def replace_list(list1, list2):
    list1[-1:] = list2
    return list1
```


This function uses Python's list slicing and assignment feature to replace the last element of the first list with the elements of the second list. The expression `list1[-1:]` returns a slice of the list from the last element to the end, and the assignment `list1[-1:] = list2` replaces these elements with the elements of `list2`. The function then returns the modified list. 

For example, if we call `replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8])`, the function will return `[1, 3, 5, 7, 9, 2, 4, 6, 8]`. 

The unit test `assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]` ensures that the function works correctly. 

Note that this function modifies the original list, it does not create a new list. If you want to create a new list without modifying the original, you can create a copy of the original list at the beginning of the function. For example, `list1_copy = list1[:]` would create a copy of `list1`. 
```python
def replace_list(list1, list2):
    list1_copy = list1[:]
    list1_copy[-1:] = list2
    return list1_copy
```  This function would return a new list without modifying the original. 
```python
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
```  This unit test would pass. 
```python
print([1, 3, 5, 7, 9, 10])  # prints [1, 3, 5, 7, 9, 10]
print(replace_list([1, 3, 5, 7, 9, 10