The problem is asking to create a function that takes a list and an integer as input, and then splits the list at the nth element. The first part of the list is then moved to the end of the list.

Here's a Python function that accomplishes this:

```python
def split_Arr(lst, n):
    if n > len(lst):
        return lst
    return lst[n:] + lst[:n]
```

This function first checks if the given integer `n` is greater than the length of the list. If it is, the function returns the original list as it is not possible to split the list at an index that is beyond its length.

If `n` is within the length of the list, the function uses Python's list slicing feature to split the list into two parts: `lst[n:]` gives the second part of the list (from the nth element to the end), and `lst[:n]` gives the first part of the list (from the start to the nth element). The function then concatenates these two parts in reverse order and returns the result.

For example, if we call `split_Arr([12,10,5,6,52,36],2)`, the function will return `[5,6,52,36,12,10]`, which is the original list with the first part moved to the end. This matches the expected output in the problem statement. 