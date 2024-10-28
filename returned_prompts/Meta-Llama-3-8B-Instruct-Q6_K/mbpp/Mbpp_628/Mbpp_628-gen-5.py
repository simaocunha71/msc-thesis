```
def replace_spaces(s):
    return s.replace(' ', '%20')
```
In this problem, we need to write a function that replaces all spaces in a given string with '%20'. The function takes a string as an argument and returns the modified string.

We can use the built-in `replace` method of Python strings to achieve this. The `replace` method replaces all occurrences of a substring with another substring. In this case, we want to replace all spaces with '%20'.

The unit test `assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'` ensures that the function works correctly. It checks that the function replaces all spaces in the given string with '%20' and returns the modified string.

Here is the solution:
```
def replace_spaces(s):
    return s.replace(' ', '%20')
```
This function takes a string `s` as an argument, replaces all spaces with '%20' using the `replace` method, and returns the modified string. The unit test ensures that the function works correctly.