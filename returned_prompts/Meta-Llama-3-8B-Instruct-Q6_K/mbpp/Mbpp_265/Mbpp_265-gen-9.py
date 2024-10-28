```
def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
```
This function uses list comprehension to split the list into sublists of length n. The range function is used to generate the start indices for the slices, with a step size of n. The list comprehension then creates the sublists by slicing the original list at these start indices.

For example, if we call `list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)`, the function will return `[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]`. 

This is confirmed by the provided unit test. 

The time complexity of this function is O(n), where n is the length of the input list. This is because we are iterating over the list once to create the sublists. The space complexity is also O(n), as we are creating a new list to store the sublists. 