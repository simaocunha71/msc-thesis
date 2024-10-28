You can use the built-in function `list()` in combination with the string. This function converts a string into a list of characters. Here is the function:

```python
def split(s):
    return list(s)
```

This function will split the string into characters and return them as a list. For example, if you call `split('python')`, it will return `['p', 'y', 't', 'h', 'o', 'n']`. This is exactly what the unit test `assert split('python') == ['p','y','t','h','o','n']` is expecting.  This function will work for any string.  



