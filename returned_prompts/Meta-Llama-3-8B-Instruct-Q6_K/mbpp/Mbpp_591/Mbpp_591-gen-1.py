```
def swap_List(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
```


The function `swap_List` takes a list as an input and checks if the list has more than one element. If it does, it swaps the first and last elements of the list. The function then returns the modified list. This function uses Python's tuple packing and unpacking feature to swap the elements. The expression `lst[0], lst[-1] = lst[-1], lst[0]` is equivalent to `temp = lst[0]; lst[0] = lst[-1]; lst[-1] = temp`, but is more concise and efficient. The unit test `assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]` ensures that the function works correctly. 





Python 3.8+:

```
def swap_List(lst):
    if len(lst) > 1:
        lst[0], *_, lst[-1] = lst
    return lst
```

This version of the function uses the unpacking operator `*` to remove all elements except the first and last from the list. This is a more concise way to swap the first and last elements, but it is only available in Python 3.8 and later. 





Python 3.7 and earlier:

```
def swap_List(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
        del lst[1:-1]
    return lst
```

This version of the function uses the same approach as the original function, but it uses the `del` statement to remove all elements except the first and last from the list. This is a more verbose way to swap the first and last elements, but it is available in all versions of Python. 





Python 3.9 and later:

```
def swap_List(lst):
    if len(lst) > 1:
        lst[:] = [lst[-1]] + lst[1:-1] + [lst[0]]
    return lst
```

This version of the function uses list slicing to create a new list that contains the elements in the correct order. This is a more concise way to swap the first and last elements, but it is only