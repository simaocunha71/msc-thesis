```
def find_char_long(s):
    return [i for i in s.split() if len(i) >= 4]
```

Explanation:
The function `find_char_long` takes a string `s` as input and splits the string into a list of words using the `split()` method. Then, it creates a new list comprehension `[i for i in s.split() if len(i) >= 4]` that filters out words that are less than 4 characters long. Finally, it returns the new list of words that are at least 4 characters long.

In the provided example, the function is called with the string `'Please move back to stream'` and the resulting list of words is compared to a set of expected words (`['Please', 'move', 'back', 'stream']`). The `set()` function is used to remove duplicate words from the result. The assertion checks if the set of expected words matches the set of words returned by the function, ensuring that the function correctly finds all words that are at least 4 characters long in the input string.

Overall, this solution provides a simple and efficient way to find all words of a certain length in a string using Python.

```python
def find_char_long(s):
    return [i for i in s.split() if len(i) >= 4]
```

This function will return a list of all words in the input string that are at least 4 characters long. In the provided example, it will return `['Please', 'move', 'back', 'stream']` as expected.

Here's how the function works:

1. The `split()` method is used to split the input string `s` into a list of words. Each word is separated by whitespace.
2. A list comprehension `[i for i in s.split() if len(i) >= 4]` is used to iterate over each word in the list and filter out words that are less than 4 characters long. The `len(i)` condition checks the length of each word `i`.
3. The resulting list of words is returned by the function.

You can use this function in your Python code to find all words that are at least 4 characters long