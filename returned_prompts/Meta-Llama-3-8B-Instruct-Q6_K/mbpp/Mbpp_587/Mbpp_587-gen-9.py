You can use the built-in tuple() function in Python to convert a list to a tuple. Here is the function:

```
def list_tuple(lst):
    return tuple(lst)
```

This function takes a list as input, converts it to a tuple using the tuple() function, and returns the resulting tuple. The unit test `assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)` confirms that this function works correctly. 

Note that the tuple() function does not modify the original list; it returns a new tuple containing the elements of the list. The original list remains unchanged. 

For example, if you have a list [1, 2, 3] and you use the list_tuple() function to convert it to a tuple, the original list remains [1, 2, 3], but the function returns the tuple (1, 2, 3). 

Here is the output of the function with the given unit test:

```
print(list_tuple([5, 10, 7, 4, 15, 3]))
(5, 10, 7, 4, 15, 3)
``` 





Here is the complete code:

```
def list_tuple(lst):
    return tuple(lst)

assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)

print(list_tuple([5, 10, 7, 4, 15, 3]))
```





Output:

```
(5, 10, 7, 4, 15, 3)
```