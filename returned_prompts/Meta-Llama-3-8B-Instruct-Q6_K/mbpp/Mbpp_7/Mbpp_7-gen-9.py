```
def find_char_long(s):
    words = s.split()
    result = [word for word in words if len(word) >= 4]
    return set(result)
```


The function works by first splitting the input string into a list of words using the `split` method. Then, it uses a list comprehension to create a new list `result` that contains only the words that have a length of at least 4 characters. Finally, it converts the `result` list into a set and returns it.

The `assert` statement checks that the function returns the correct result for the input string `'Please move back to stream'`. The expected result is the set `{'Please', 'move', 'back', 'stream'}`. The `assert` statement ensures that the function returns this set, which means that it correctly identifies all words that are at least 4 characters long.