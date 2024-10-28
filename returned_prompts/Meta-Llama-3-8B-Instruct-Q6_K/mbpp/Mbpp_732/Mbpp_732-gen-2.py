```
def replace_specialchar(s):
    s = s.replace(" ", ":")
    s = s.replace(",", ":")
    s = s.replace(".", ":")
    return s
```


The function `replace_specialchar` takes a string `s` as input and returns a new string where all occurrences of spaces, commas, and dots are replaced with a colon. The function uses the `replace` method of the string to replace each character. The `replace` method takes two arguments: the character to be replaced and the replacement character. The method returns a new string with all occurrences of the specified character replaced with the replacement character. The function returns the new string. The unit test `assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')` checks if the function works correctly. It asserts that the function returns 'Python:language::Programming:language:' when given 'Python language, Programming language.' as input. This test ensures that the function correctly replaces spaces, commas, and dots with a colon. 