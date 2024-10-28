```
def replace_spaces(s):
    return s.replace(' ', '%20')
```


The provided unit test `assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'` suggests that the function should replace all spaces in the input string with '%20'. 

The `replace` method in Python is used to replace a specified phrase with another specified phrase. In this case, the specified phrase is a space (' ') and the replacement phrase is '%20'. 

The function takes a string `s` as input and returns a new string where all spaces are replaced with '%20'. This is achieved by calling the `replace` method on the input string `s` and returning the result. 
```python
def replace_spaces(s):
    return s.replace(' ', '%20')
``` 





This function will replace all spaces in the input string with '%20'. For example, if the input string is "My Name is Dawood", the output will be 'My%20Name%20is%20Dawood'. 

The function is simple and efficient, as it uses the built-in `replace` method of the string class in Python, which has a time complexity of O(n), where n is the length of the input string. Therefore, the overall time complexity of the function is O(n), making it suitable for large input strings. 





The function does not modify the original string, but returns a new string with the spaces replaced. This is because strings in Python are immutable, which means they cannot be changed in-place. Instead, a new string is created and returned. This is a good practice in Python, as it makes the code more predictable and easier to understand.