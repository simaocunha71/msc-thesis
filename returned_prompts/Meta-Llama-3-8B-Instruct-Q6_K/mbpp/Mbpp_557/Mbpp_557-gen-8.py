```
def toggle_string(s):
    return s.swapcase()
```
The function `toggle_string` takes a string `s` as input and returns a new string where all characters are toggled in case. For example, if the input string is "Python", the output will be "pYTHON". 

The `swapcase()` method of the string is used to achieve this. It returns a copy of the string where all uppercase characters are converted to lowercase and vice versa. 

The unit test `assert toggle_string("Python")==("pYTHON")` ensures that the function works correctly.  It checks if the output of the function with input "Python" is indeed "pYTHON". 

This function is case-sensitive, i.e., it will not convert non-ASCII characters to their case-folded equivalents. For example, the German uppercase letter "Ä" will remain uppercase in the output string, and the German lowercase letter "ä" will remain lowercase. If you need to handle non-ASCII characters, you will need to use a more complex solution that takes into account the specific character set and locale. 