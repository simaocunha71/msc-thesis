```
def is_samepatterns(patterns, sequence):
    return all(patterns[i] == sequence[i] for i in range(len(patterns)))
```
This function uses the built-in `all` function in Python, which returns `True` if all elements of the iterable (in this case, a generator expression) are true. The generator expression `patterns[i] == sequence[i] for i in range(len(patterns))` checks if each element in the `patterns` list is equal to the corresponding element in the `sequence` list. If all elements are equal, the function returns `True`; otherwise, it returns `False`. 

For example, `is_samepatterns(["red","green","green"], ["a", "b", "b"])` returns `True` because the sequences match. 

Note that this function assumes that the `patterns` and `sequence` lists have the same length. If they don't, the function will raise an `IndexError` when trying to access elements outside the list bounds. You may want to add error checking to handle this case, depending on your specific requirements. 

The unit test `assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True` checks whether the function returns the correct result for a given pair of patterns and sequence. 