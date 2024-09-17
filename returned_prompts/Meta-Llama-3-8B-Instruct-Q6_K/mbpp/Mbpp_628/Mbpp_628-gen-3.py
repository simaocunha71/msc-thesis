```
def replace_spaces(s):
    return s.replace(' ', '%20')
```


The problem is asking you to create a function that takes a string as an input and replaces all the spaces in the string with '%20'. 

The unit test provided suggests that the function should return the modified string. 

The solution is to use the built-in `replace` method of Python strings, which replaces all occurrences of the first argument with the second argument. In this case, we replace all spaces with '%20'.

Here is the Python function that accomplishes this:

```
def replace_spaces(s):
    return s.replace(' ', '%20')
```

This function takes a string `s` as an argument, replaces all spaces with '%20', and returns the modified string. 

For example, if you call `replace_spaces("My Name is Dawood")`, it will return `'My%20Name%20is%20Dawood'`. 

This solution passes the provided unit test. 