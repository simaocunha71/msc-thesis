```
def replace_specialchar(s):
    return s.replace(" ", ":").replace(",", ":").replace(".", ":")
```


The function replace_specialchar takes a string s as an input and returns a new string where all occurrences of spaces, commas, or dots are replaced with a colon.

The unit test provided is:
```
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
```
This test checks if the function correctly replaces all occurrences of spaces, commas, or dots with a colon. The expected output is 'Python:language::Programming:language:'. 

The function uses the built-in string method replace() to replace all occurrences of the specified characters with the specified replacement. The replace() method returns a copy of the string where all occurrences of a substring are replaced with another substring. 

In this case, the function replaces all occurrences of spaces, commas, or dots with a colon. The order of the replace() method calls does not matter in this case, because the replace() method returns a new string and does not modify the original string. However, for clarity and to avoid potential issues, it's recommended to replace the characters in the order of their appearance in the string. 

The function does not modify the original string, it returns a new string with the replacements. This is evident from the unit test provided, which checks the output of the function, not the original string. 





Note: This function assumes that the input string does not contain any characters that have a special meaning in the context of the replace() method, such as backslashes or special characters in regular expressions. If the input string can contain such characters, the function may need to be modified to handle them correctly.