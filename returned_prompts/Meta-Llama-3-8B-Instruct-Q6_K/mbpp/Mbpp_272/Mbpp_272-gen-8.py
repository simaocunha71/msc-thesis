You can solve this problem with the following function:

```python
def rear_extract(tuples_list):
    return [tup[-1] for tup in tuples_list]
``` 

This function uses a list comprehension to iterate over each tuple in the input list, and for each tuple, it returns the last element (i.e., the "rear" element) using Python's indexing. The resulting list of "rear" elements is then returned. 

For example, given the input `[(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]`, this function would return `[21, 20, 19]`. This result is confirmed by the provided unit test. 

Note: Python's indexing starts at 0, so the last element of a tuple (or list) is accessed with an index of -1. This is why `tup[-1]` is used in the list comprehension.  If you were to use `tup[0]` instead, you would get the first element of each tuple, not the last.  If you were to use `tup[1]` instead, you would get the second element of each tuple, not the last.  And so on.  This is a common and convenient way to access elements in Python lists and tuples.  It's also worth noting that Python's indexing is 0-based, meaning that the first element is at index 0, not 1.  This is different from some other programming languages, where the first element may be at index 1.  If you're not used to this, it may take some getting used to.  But once you get the hang of it, it can be a powerful and flexible way to work with data in Python. 