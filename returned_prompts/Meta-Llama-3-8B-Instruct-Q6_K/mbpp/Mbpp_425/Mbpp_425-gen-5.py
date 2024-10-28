```
def count_element_in_list(lst, target):
    return sum(1 for sublist in lst if target in sublist)
```


This function counts the number of sublists in the input list `lst` that contain the element `target`. It uses a generator expression to iterate over the sublists and a sum to count the number of sublists that contain the target element. The unit test `assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3` demonstrates the function's behavior. It counts the number of sublists that contain the element `1`, which is `3`. 





Note: This function assumes that the input list is non-empty. If the input list can be empty, you might want to add a check for that case and return a specific value, for example, 0.