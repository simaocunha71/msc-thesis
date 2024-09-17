You can use the built-in function set() in Python, which returns a set object containing all items from the list. If the length of the set is equal to the length of the list, then all elements in the list are unique. Here is a Python function that checks this:

```python
def all_unique(lst):
    return len(lst) == len(set(lst))
```

This function works by converting the list to a set, which automatically removes any duplicate elements. It then compares the length of the original list to the length of the set. If they are equal, then all elements in the list are unique. If they are not equal, then there were duplicate elements in the list. 

For example, you can test this function with the following code:

```python
print(all_unique([1,2,3]))  # Returns: True
print(all_unique([1,2,2]))  # Returns: False
```

The unit test provided in the question, `assert all_unique([1,2,3]) == True`, will also pass with this function. 

Please note that this function is case sensitive and considers elements as unique based on their values, not their positions in the list. If you want to check for uniqueness based on the positions in the list, you would need a different approach. 