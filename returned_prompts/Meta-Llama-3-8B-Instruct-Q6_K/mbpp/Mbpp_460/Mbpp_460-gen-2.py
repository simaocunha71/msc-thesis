```
def Extract(lst):
    return [sublist[0] for sublist in lst]
```



The function `Extract` takes a list of lists as input and returns a new list containing the first element of each sublist. The function uses a list comprehension to iterate over each sublist in the input list and extract the first element. The result is a new list containing these first elements. The unit test `assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]` ensures that the function works correctly.