You can use list comprehension along with the built-in function `list()` and `iter()` to achieve this. Here is the Python function that splits a string into characters:

```
def split(s):
    return list(iter(s))
```

This function works by creating an iterator over the string `s` using `iter(s)`, and then converting that iterator into a list using `list()`. The result is a list of characters, each one from the original string.

For example, if you call `split('python')`, it will return the list `['p','y','t','h','o','n']`. This is confirmed by the unit test `assert split('python') == ['p','y','t','h','o','n']`. 