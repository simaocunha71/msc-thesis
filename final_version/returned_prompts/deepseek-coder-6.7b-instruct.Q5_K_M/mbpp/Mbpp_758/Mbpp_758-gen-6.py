Here is the Python function for the problem:

```python
def unique_sublists(lst):
    count_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in count_dict:
            count_dict[tuple_sublist] += 1
        else:
            count_dict[tuple_sublist] = 1
    return count_dict
```

This function works by creating a dictionary where each key is a tuple representation of a sublist from the original list and each value is the count of occurrences of that sublist in the original list. If the tuple representation of a sublist is already a key in the dictionary, the function increments the value by one; otherwise, it adds a new key-value pair to the dictionary with a value of one. The function then returns the dictionary.
"""

