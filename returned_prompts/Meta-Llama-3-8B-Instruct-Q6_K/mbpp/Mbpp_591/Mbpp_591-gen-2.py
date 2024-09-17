```
def swap_List(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
```
This function checks if the list has more than one element. If it does, it swaps the first and last elements using tuple packing and unpacking. Finally, it returns the modified list. The unit test `assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]` ensures that the function works correctly. 