```
def replace_spaces(s):
    return s.replace(' ', '%20')
```



The problem is asking you to write a function that replaces all spaces in a given string with '%20'. 

The unit test provided, `assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'`, helps clarify the problem by giving an example of how the function should behave.

Here's a simple Python function that solves the problem using the `replace` method of the string class:

```
def replace_spaces(s):
    return s.replace(' ', '%20')
```

This function takes a string `s` as input, replaces all spaces in `s` with '%20', and returns the resulting string. The `replace` method returns a copy of the string where all occurrences of a substring have been replaced with another substring. In this case, we're replacing all spaces with '%20'. 