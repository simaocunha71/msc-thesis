```
def split_two_parts(lst, L):
    return tuple([lst[:L], lst[L:]])
```





The function takes a list and an integer L as input. It then returns a tuple containing two lists: the first part of the input list (up to the length L) and the remaining part of the list.

The unit test `assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])` ensures that the function works correctly by checking that the output for a given input is as expected.

The function uses Python's list slicing feature to create the two parts of the list. The expression `lst[:L]` returns a new list that is a slice of the input list up to the index L, and the expression `lst[L:]` returns a new list that is a slice of the input list starting from the index L to the end of the list. The `tuple` function is then used to convert the two lists into a tuple.