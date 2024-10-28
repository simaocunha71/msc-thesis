```
def rear_extract(tuples_list):
    return [x[-1] for x in tuples_list]
```


The problem is asking you to create a function that takes a list of tuples as an input and returns a list containing the last element of each tuple. For example, if you have the tuple (1, 'Rash', 21), the function should return 21.

The unit test provided helps to clarify the problem by showing that the function should return a list containing the last element of each tuple. In this case, the function should return [21, 20, 19] for the input [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)].

The solution to this problem is a list comprehension. This is a concise way to create a new list in Python by performing an operation on each item in an existing list. In this case, the operation is to take the last element of each tuple.

Here is the solution:
```
def rear_extract(tuples_list):
    return [x[-1] for x in tuples_list]
```


This function uses a list comprehension to iterate over each tuple in the input list. For each tuple, it takes the last element (which is accessed using the index -1) and adds it to the output list. The resulting list is then returned by the function.