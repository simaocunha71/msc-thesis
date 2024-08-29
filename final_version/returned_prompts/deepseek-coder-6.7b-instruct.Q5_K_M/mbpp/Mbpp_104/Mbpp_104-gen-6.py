Here is the Python function for the problem:

```python
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]
```

This function uses list comprehension to iterate over each sublist in the given list, and the built-in sorted function to sort each sublist. The sorted sublists are returned in a new list.

You can test the function with the provided example:

```python
print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))
```

This will output:

```
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```
Which confirms that the function works as expected.

The time complexity of this function is O(n*m*log(m)), where n is the number of sublists in the list and m is the average length of the sublists. This is because it iterates over each sublist, and the sorted function has a time complexity of O(m*log(m)). The space complexity is O(n*m), as it creates a new list with the same size as the input list.
"""

