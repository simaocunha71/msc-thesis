```
def count_integer(lst):
    return sum(isinstance(x, int) for x in lst)
```


The function `count_integer(lst)` takes a list `lst` as an argument and returns the number of integer elements in the list. 

The `isinstance(x, int)` function checks if the element `x` is an integer or not. The `sum()` function then counts the number of `True` values returned by `isinstance(x, int)` for all elements in the list.

For example, when the list is `[1,2,'abc',1.2]`, the function returns `2` because there are two integer elements in the list.  The unit test `assert count_integer([1,2,'abc',1.2]) == 2` also confirms this. 