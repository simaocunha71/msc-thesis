The task is to write a function that takes a list as an input and returns a tuple. The function should not modify the original list and should not use any external libraries.

The unit test provided, `assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)`, suggests that the function should return a tuple that contains the same elements as the input list.

Here's a simple Python function that accomplishes this:

```python
def list_tuple(lst):
    return tuple(lst)
```

This function uses Python's built-in `tuple` function to convert the input list to a tuple. The `tuple` function returns a tuple containing all elements from the input iterable (in this case, the list). The original list remains unchanged, as required. The unit test provided should pass with this function. 