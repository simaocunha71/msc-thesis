```
def ascii_value(char):
    return ord(char)
```


The problem asks to write a function that takes a character as input and returns its ASCII value. 

The unit test `assert ascii_value('A')==65` suggests that the function should work for uppercase letters. 

The built-in Python function `ord()` is used to get the ASCII value of a character. So, the solution is a simple function that takes a character as input and returns its ASCII value using `ord()`. 

For example, the ASCII value of 'A' is 65, so `ascii_value('A')` should return 65. 

Here is the Python code for the function:
```
def ascii_value(char):
    return ord(char)
``` 





This function works for any character, not just uppercase letters. It will return the ASCII value of any character that is passed to it. For example, `ascii_value('a')` will return 97, which is the ASCII value of 'a'. Similarly, `ascii_value('0')` will return 48, which is the ASCII value of '0'.