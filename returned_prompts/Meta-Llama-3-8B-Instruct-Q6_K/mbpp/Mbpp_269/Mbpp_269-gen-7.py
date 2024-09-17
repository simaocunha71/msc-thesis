```
def ascii_value(char):
    return ord(char)
```


The task is to create a function that takes a character as input and returns its ASCII value.

The unit test provided is `assert ascii_value('A')==65`, which means the function should return the ASCII value of the character 'A', which is 65.

The built-in function `ord()` in Python returns the ASCII value of a character. Therefore, the solution is to simply use `ord(char)` to get the ASCII value of the character.

Here is the Python function:

```
def ascii_value(char):
    return ord(char)
```


This function takes a character as input, uses the `ord()` function to get its ASCII value, and returns the result. The unit test provided will pass with this function.