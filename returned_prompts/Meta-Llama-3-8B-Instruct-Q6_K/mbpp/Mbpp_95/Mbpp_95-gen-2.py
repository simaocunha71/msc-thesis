```
def Find_Min_Length(list_of_lists):
    return min(len(sublist) for sublist in list_of_lists)
```


The function `Find_Min_Length` takes a list of lists as input and returns the length of the smallest list in the list of lists. The function uses a generator expression to iterate over the sublists in the list of lists, calculates the length of each sublist using the `len` function, and then uses the `min` function to find the smallest length. The result is returned as the output of the function.

For example, if the input is `[[1],[1,2]]`, the function will return `1`, which is the length of the smallest list in the list of lists. The unit test `assert Find_Min_Length([[1],[1,2]]) == 1` ensures that the function works correctly in this case.