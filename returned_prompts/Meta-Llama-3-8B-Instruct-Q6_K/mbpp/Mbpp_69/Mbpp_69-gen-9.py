```
def is_sublist(lst, sublst):
    return sublst in [lst[i:i+len(sublst)] for i in range(len(lst))]
```

This function uses list comprehension to generate all possible sublists of the given list and checks if the given sublist is present in that list. If it is, the function returns True; otherwise, it returns False.

The unit test `assert is_sublist([2,4,3,5,7],[3,7])==False` fails because the sublist `[3,7]` is not present in the given list. The function correctly returns False in this case.