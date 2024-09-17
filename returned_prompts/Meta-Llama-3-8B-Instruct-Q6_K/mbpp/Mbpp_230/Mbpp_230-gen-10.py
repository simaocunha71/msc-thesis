```
def replace_blank(s, c):
    return s.replace(' ', c)
```
The problem is asking you to create a function that takes a string and a character as input, and returns the string with all blank spaces replaced with the given character.

The unit test provided is `assert replace_blank("hello people",'@')==("hello@people")`, which means that the function should replace all blank spaces in the string "hello people" with the character '@', resulting in "hello@people".

To solve this problem, we can use the built-in `replace` function in Python, which replaces a specified phrase with another specified phrase. In this case, we want to replace blank spaces with the given character. So, we simply call `s.replace(' ', c)` to replace all occurrences of blank spaces with the character `c`, and return the resulting string. 

Here is the solution:
```
def replace_blank(s, c):
    return s.replace(' ', c)
``` 





This function will replace all blank spaces in the string `s` with the character `c` and return the resulting string. For example, if you call `replace_blank("hello people", "@")`, it will return `"hello@people"`.