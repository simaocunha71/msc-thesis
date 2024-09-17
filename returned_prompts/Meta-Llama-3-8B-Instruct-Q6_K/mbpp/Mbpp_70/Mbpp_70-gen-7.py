```
def get_equal(tuples):
    return len(set(map(len, tuples))) == 1
```



The problem asks you to create a function that checks if all the tuples in a given list have the same length. 

The function should return a boolean value indicating whether all the tuples have the same length or not. 

The unit test `assert get_equal([(11, 22, 33), (44, 55, 66)]) == True` suggests that the function should return True if all tuples have the same length, and False otherwise.

Here's a Python solution for this problem:

```
def get_equal(tuples):
    return len(set(map(len, tuples))) == 1
```

This function works by first using the `map` function to apply the `len` function to each tuple in the list, effectively getting a list of lengths. The `set` function is then used to remove any duplicates from this list. If all the tuples had the same length, the set will contain only one element. The function returns True if the set contains only one element, and False otherwise. 