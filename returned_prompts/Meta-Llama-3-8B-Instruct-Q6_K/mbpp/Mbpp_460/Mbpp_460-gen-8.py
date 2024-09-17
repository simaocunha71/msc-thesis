```
def Extract(lists):
    return [sublist[0] for sublist in lists]
```


The function Extract() takes a list of lists as an argument and returns a new list with the first element of each sublist. The function uses a list comprehension to iterate over the sublists and extract the first element of each. The unit test `assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]` ensures that the function works correctly.  The function can be used like this:
```
print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))  # Output: [1, 3, 6]
``` 