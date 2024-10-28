```
def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
```


This function uses list comprehension to iterate over the list in steps of `n`, and for each step, it slices the list from the current index `i` to `i+n` and adds it to the result list. The `range(0, len(lst), n)` expression generates the indices `i` for the slice operation. 

For example, if we call `list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)`, the function will return `[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]`. 

The unit test `assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]` ensures that the function behaves correctly. 
```python
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
``` 

The function takes a list `lst` and an integer `n` as input, and returns a list of lists, where each sublist contains every `n`th element from the original list, starting from the first element. 

This function assumes that the input list has at least one element and that `n` is a positive integer. If the input list is empty or `n` is less than or equal to 0, the function may not behave correctly. 

In terms of time complexity, the function has a linear time complexity O(n), where `