```
def remove_whitespaces(s):
    return s.replace(" ", "")
```
This function uses the built-in string method `replace()` to replace all occurrences of whitespace characters with an empty string, effectively removing them. The unit test provided ensures that the function works correctly by comparing its output with the expected output for the input string `' Google    Flutter '`. 

When the function is called with this input string, it returns the string `'GoogleFlutter'`, which is the expected output. 

The time complexity of this function is O(n), where n is the length of the input string, because it needs to iterate over the entire string to find and replace all occurrences of whitespace characters. The space complexity is O(1), because it only uses a constant amount of space to store the function's local variables, regardless of the size of the input string. 