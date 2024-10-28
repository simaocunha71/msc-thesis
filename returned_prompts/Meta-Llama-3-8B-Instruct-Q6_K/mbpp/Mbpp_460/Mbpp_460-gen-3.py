```
def Extract(lst):
    return [sublist[0] for sublist in lst]
```


Explanation:
The task is to create a function that takes a list of sublists as input and returns a new list containing the first element of each sublist.

The unit test provided helps in understanding the expected output. It shows that the function should return a list `[1, 3, 6]` when given the input `[[1, 2], [3, 4, 5], [6, 7, 8, 9]]`.

To solve this problem, we can use a list comprehension in Python. The list comprehension iterates over each sublist in the input list and selects the first element of each sublist. The resulting list of first elements is then returned.

Here's the Python function that implements this solution:

```python
def Extract(lst):
    return [sublist[0] for sublist in lst]
```

This function takes a list `lst` as input, and returns a new list containing the first element of each sublist in `lst`. The list comprehension `[sublist[0] for sublist in lst]` iterates over each sublist `sublist` in `lst`, and selects the first element `sublist[0]` of each sublist. The resulting list of first elements is then returned.