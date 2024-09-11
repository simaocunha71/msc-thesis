Here is one way you can do it:

```python
def interleave_lists(list1, list2, list3):
    """
    Interleave 3 lists of the same length into a single flat list.
    """
    result = []
    i = 0
    while i < len(list1):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
        i += 1
    return result
```

To test it, you can use the following code:

```python
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
```

This will return `True`, as expected.

In this function, we initialize an empty list `result` to store the interleaved lists. We also initialize a variable `i` to keep track of the current index in the input lists. We then use a while loop to iterate through the input lists until we reach the end of the shortest list. Inside the loop, we append the current element from each input list to `result` in turn, and increment the index `i` by 1. Finally, we return the interleaved list `result`.

By using this function, you can interleave any three lists of the same length into a single flat list.

"""

# Your code goes here

```python
def interleave_lists(list1, list2, list3):
    """
    Interleave 3 lists of the same length into a single flat list.
    """
    result = []
    i = 0
    while i <