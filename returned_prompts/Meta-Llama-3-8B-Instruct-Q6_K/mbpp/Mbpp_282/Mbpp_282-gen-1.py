```
def sub_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    return [a-b for a, b in zip(list1, list2)]
```


The function `sub_list` subtracts two lists element-wise. It first checks if the lists are of the same length. If not, it raises a `ValueError`. Then, it uses a list comprehension to create a new list where each element is the difference between the corresponding elements in the input lists. The `zip` function is used to iterate over the elements of the two lists in parallel. The result is a list of the differences between corresponding elements in the input lists. For example, `sub_list([1, 2, 3],[4,5,6])` returns `[-3, -3, -3]`.  This solution passes the given unit test. 