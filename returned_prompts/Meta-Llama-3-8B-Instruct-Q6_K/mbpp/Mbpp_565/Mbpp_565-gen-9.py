You can use the built-in function list() along with the string to split it into individual characters. Here is the Python function:

```
def split(s):
    return list(s)
```

This function takes a string as input, and returns a list of characters. The unit test `assert split('python') == ['p','y','t','h','o','n']` ensures that the function works correctly. For example, `split('python')` should return `['p','y','t','h','o','n']`. 

Note that this function is quite simple, but it should work as expected. If you need more complex functionality, you might need to write a more complex function.  For example, if you want to split the string into characters and ignore certain characters, you would need to write a more complex function that iterates over the string and checks each character to see if it should be included in the output list.  However, for the simple case of splitting a string into individual characters, this function should work fine.  It is also worth noting that this function does not handle the case where the input is not a string.  If the input is not a string, the function will raise an error.  You might want to add some error checking code to handle this case, depending on how you want the function to behave.  For example, you might want the function to raise an error if the input is not a string, or you might want the function to return an empty list or some other default value.  It depends on how you want the function to behave in this case.  You could add a try/except block to handle this case, for example:

```
def split(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return list(s)
```

This will raise a ValueError if the input is not a string.  You could also add some default behavior, such as returning an empty list, like this:

```
def split(s):
    if not isinstance(s, str):
        return []
    return list(s)
```

This will return an empty list if the input is not a string.  There are many ways to handle this case, and the best approach will depend on how you want the function to behave.  It's up to you to decide how you want the function to behave in this case.  You could also add some documentation to the function to explain how it behaves in this case, which