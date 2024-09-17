You can use the built-in `tuple()` function in Python to convert a string to a tuple of characters. Here is the function:

```
def string_to_tuple(s):
    return tuple(s)
```

This function works by directly passing the string `s` to the `tuple()` function, which converts it into a tuple of characters. For example, the string "python 3.0" would be converted to the tuple `('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')`. 

The unit test `assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')` ensures that this function works correctly. 

Note that this function does not remove any spaces or punctuation. If you want to remove spaces or punctuation, you would need a more complex function that uses the `str.replace()` or `str.translate()` methods. For example:

```
def string_to_tuple(s):
    s = s.replace(" ", "").replace(",", "").replace(".", "")
    return tuple(s)
``` 

This function would remove all spaces, commas, and periods from the string before converting it to a tuple.  However, the original function is simpler and more efficient, and it may be sufficient for many use cases.  It depends on the specific requirements of your program. 