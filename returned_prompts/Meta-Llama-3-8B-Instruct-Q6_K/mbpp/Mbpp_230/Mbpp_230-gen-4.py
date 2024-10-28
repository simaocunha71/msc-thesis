```
def replace_blank(s, c):
    return s.replace(" ", c)
```
This function uses the built-in string method `replace()` which replaces a specified phrase with another specified phrase. In this case, it replaces all occurrences of a blank space (`" "`) with the specified character (`c`). The function returns the modified string. 

For example, if the input string is "hello people" and the character is "@", the function will return "hello@people". 

The unit test `assert replace_blank("hello people",'@')==("hello@people")` ensures that the function behaves as expected. 

This function does not handle any exceptions, so if the input is not a string or if the character is not a single character, the function may not work as expected. You could add error handling code to deal with these cases if you want. 