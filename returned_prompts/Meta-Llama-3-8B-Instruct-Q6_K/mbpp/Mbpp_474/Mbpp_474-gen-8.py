```
def replace_char(s, old, new):
    return s.replace(old, new)
```


This function takes a string `s`, an old character `old`, and a new character `new` as inputs. It returns a new string where all occurrences of `old` are replaced with `new`.

The unit test `assert replace_char("polygon",'y','l')==("pollgon")` ensures that the function works correctly. The test checks if the function replaces all 'y's in "polygon" with 'l's and returns "pollgon". 

In the solution, the `replace` method of the string is used to replace all occurrences of `old` with `new`. This method returns a new string with the replacements, leaving the original string unchanged. 

The function is designed to be general-purpose, allowing the user to specify any old and new characters. It can be used to replace any character in a string, not just a single character. For example, it could be used to replace all occurrences of a word with another word. 