```
def add_tuple(lst, tup):
    return lst + list(tup)
```


This function uses the '+' operator to concatenate the list and the tuple. The '+' operator is overloaded for lists and tuples in Python, and it returns a new list containing all elements from both operands. The list() function is used to convert the tuple to a list, so that the '+' operator can be used. The result is a new list containing all elements from the original list and the tuple. For example, add_tuple([5, 6, 7], (9, 10)) would return [5, 6, 7, 9, 10].