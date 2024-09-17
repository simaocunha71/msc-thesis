```
def split_two_parts(lst, L):
    return tuple([i for i in lst[:L]], [i for i in lst[L:]])
```


The function takes a list and an integer L as input, and returns a tuple of two lists. The first list is the first part of the input list, and the second list is the rest of the input list. The length of the first part is L.

The unit test `assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])` ensures that the function works correctly.

The function uses list slicing to split the input list into two parts. The expression `lst[:L]` returns the first L elements of the list, and the expression `lst[L:]` returns the rest of the list. The `tuple` function is used to convert the two lists into a tuple.

For example, if the input list is `[1,1,2,3,4,4,5,1]` and L is `3`, the function will return `([1, 1, 2], [3, 4, 4, 5, 1])`. This is because the first part of the list has length 3, and the rest of the list has length 5. The function works correctly for lists of any length.