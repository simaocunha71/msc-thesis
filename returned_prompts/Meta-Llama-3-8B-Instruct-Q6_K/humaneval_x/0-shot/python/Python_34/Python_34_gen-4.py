    return sorted(set(l))

Note: This solution uses the built-in Python functions `set()` and `sorted()`. The `set()` function removes duplicates from a list, and the `sorted()` function sorts the elements of a list in ascending order. The combined effect is that the function returns a sorted list of unique elements. The unit test provided ensures that the function works as expected. For example, the test `unique([5, 3, 5, 2, 3, 3, 9, 0, 123])` checks that the function returns the expected output `[0, 2, 3, 5, 9, 123]`. 





