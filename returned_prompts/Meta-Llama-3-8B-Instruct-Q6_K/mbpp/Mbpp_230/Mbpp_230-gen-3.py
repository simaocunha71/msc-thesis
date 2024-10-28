```
def replace_blank(s, c):
    return s.replace(" ", c)
```


The problem is asking you to create a function that takes a string and a character as input, and returns the string with all blank spaces replaced with the given character.

The unit test provided helps to clarify the problem. It shows that the function should replace all blank spaces in the input string with the given character.

Here's a simple solution using the `replace` method of Python strings:
```
def replace_blank(s, c):
    return s.replace(" ", c)
```
This function uses the `replace` method to replace all occurrences of the blank space character (" ") in the input string `s` with the given character `c`. The resulting string is then returned.