```
def substract_elements(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i] - t2[i])
    return tuple(result)
```



The problem asks you to create a function that takes two tuples as input and returns a new tuple where each element is the difference between the corresponding elements in the input tuples.

The unit test `assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)` helps to clarify the problem by showing that the function should subtract the elements of the second tuple from the elements of the first tuple.

Here's a Python function that solves the problem:

```
def substract_elements(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i] - t2[i])
    return tuple(result)
```

This function iterates over the indices of the input tuples, subtracts the corresponding elements of the two tuples, and adds the result to a new list. Finally, it converts the list to a tuple and returns it.