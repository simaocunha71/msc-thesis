The problem is asking to write a function that takes a variable number of lists as input and returns the total count of lists.
The unit test `assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4` suggests that the function should count the number of lists, not the number of elements in each list.

Here is a simple solution:
```
def count_list(*args):
    return len(args)
```
This function uses the `*args` syntax to accept a variable number of arguments, which are then counted using the `len` function. The result is the total count of lists.