```
def Find_Min_Length(list_of_lists):
    return min(len(lst) for lst in list_of_lists)
```



The problem asks you to write a function that finds the length of the smallest list in a list of lists. 

The given unit test `assert Find_Min_Length([[1],[1,2]]) == 1` helps to clarify the problem. It shows that the function should return the length of the smallest list.

Here is a Python solution for the problem:

```Python
def Find_Min_Length(list_of_lists):
    return min(len(lst) for lst in list_of_lists)
```

This function uses a generator expression to iterate over the lists in the list of lists. For each list, it calculates the length using the `len` function. The `min` function is then used to find the smallest length. This smallest length is the length of the smallest list in the list of lists. 