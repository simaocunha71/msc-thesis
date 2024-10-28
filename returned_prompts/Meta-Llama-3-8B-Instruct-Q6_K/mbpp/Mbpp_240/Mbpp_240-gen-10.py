```
def replace_list(lst1, lst2):
    lst1[-1:] = lst2
    return lst1
```
The function `replace_list` takes two lists as input, `lst1` and `lst2`. It replaces the last element of `lst1` with the elements of `lst2`. The `lst1[-1:]` syntax is used to get the last element of `lst1` and the `lst1[-1:] = lst2` syntax is used to replace it with the elements of `lst2`. The modified list `lst1` is then returned. 

This function passes the given unit test:
```
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]
``` 