```
def find_char_long(s):
    return set(word for word in s.split() if len(word) >= 4)
```


The function `find_char_long(s)` takes a string `s` as input, splits it into words using the `split()` method, and then uses a generator expression to filter out words that are less than 4 characters long. The resulting set of words is returned.

The unit test `assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])` ensures that the function correctly identifies all words that are at least 4 characters long in the given string. The `assert` statement checks if the set of words returned by the function is equal to the expected set of words. If the sets are not equal, the `assert` statement raises an `AssertionError`. In this case, the function correctly identifies all words that are at least 4 characters long, so the `assert` statement passes without raising an error.