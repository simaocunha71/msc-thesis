You can use the extend method to add the list to the tuple. The extend method modifies the tuple in-place. Here is the function:

```
def add_lists(lst, tup):
    return tup + tuple(lst)
```

This function converts the list to a tuple and then adds it to the original tuple. The result is a new tuple that contains all elements from the original tuple and the list. The extend method is not used here because it modifies the tuple in-place and the problem statement requires the original tuple to remain unchanged.

The unit test `assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)` ensures that the function behaves correctly. It checks that the function adds the elements from the list to the end of the tuple. If the function works correctly, this test will pass. If the function does not work correctly, this test will fail, indicating that the function needs to be modified. 





