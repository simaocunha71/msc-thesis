```
def split_two_parts(lst, L):
    return (lst[:L], lst[L:])
```


The function `split_two_parts` takes a list `lst` and an integer `L` as input, and returns a tuple containing two lists. The first list is a slice of the input list `lst` from the start to index `L`, and the second list is a slice of the input list `lst` from index `L` to the end. This ensures that the length of the first part of the list is `L`. The unit test `assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])` confirms this behavior. 

For example, if the input list is `[1,1,2,3,4,4,5,1]` and `L` is `3`, the function will return `([1, 1, 2], [3, 4, 4, 5, 1])`. 

Note that the function does not check if the length of the input list is less than or equal to `L`. If the length of the input list is less than `L`, the function will still return a tuple with two lists, but the length of the first list will be equal to the length of the input list, and the second list will be empty. For example, if the input list is `[1, 1, 2]` and `L` is `5`, the function will return `([1, 1, 2], [])`. 

In this case, the function does not raise an error or return an error message, it simply returns the resulting lists in a tuple. This behavior is consistent with the provided unit test. 

If you want the function to raise an error when the length of the input list is less than `L`, you can add a check at the beginning of the function. For example:

```
def split_two_parts(lst, L):
    if L > len(lst):
        raise ValueError("Length of the input list is less than L")
    return (lst[:L], lst[L:])
``` 

This modified function will raise a `ValueError` with the message "Length of the input list is less than L" when the length of the input list is less than `L`. 

However, this is not necessary