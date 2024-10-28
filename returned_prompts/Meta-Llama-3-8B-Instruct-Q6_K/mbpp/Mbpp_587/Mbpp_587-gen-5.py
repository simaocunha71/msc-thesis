You can use the built-in `tuple()` function in Python to convert a list to a tuple. Here's how you can do it:

```
def list_tuple(lst):
    return tuple(lst)
```

This function takes a list as an argument and returns a tuple with the same elements. The unit test `assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)` ensures that the function works correctly. 

For example, if you call `list_tuple([5, 10, 7, 4, 15, 3])`, it will return the tuple `(5, 10, 7, 4, 15, 3)`. 

This function works for lists of any length, not just the one shown in the unit test. It also works for lists containing any type of elements, not just integers. The elements of the list are converted to a tuple in the same order they appear in the list. 

The `tuple()` function is a built-in function in Python that is designed specifically for converting lists to tuples. It is a simple and efficient way to do this conversion. 