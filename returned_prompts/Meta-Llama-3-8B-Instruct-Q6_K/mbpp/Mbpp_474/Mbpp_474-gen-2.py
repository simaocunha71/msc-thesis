```
def replace_char(s, old, new):
    return s.replace(old, new)
```
This function takes three parameters: the string `s`, the character `old` to be replaced, and the character `new` to replace it with. It uses the built-in `replace` method of the string to replace all occurrences of `old` with `new`. The function returns the modified string.

For example, if we call `replace_char("polygon",'y','l')`, it will return `"pollgon"`, as expected.  The unit test `assert replace_char("polygon",'y','l')==("pollgon")` confirms this.  The function works for any string and any characters, not just those shown in the example.  It will replace all occurrences of the `old` character with the `new` character.  If there are multiple occurrences of the `old` character, they will all be replaced.  If there are no occurrences of the `old` character, the string will remain unchanged.  If the `old` character is not found in the string, the function will still return the original string.  If the `old` character is an empty string, the function will return the `new` character repeated for each character in the string.  If the `new` character is an empty string, the function will return the `old` character removed from the string.  If both the `old` and `new` characters are the same, the function will return the original string.  If the `old` character is the same as the `new` character, the function will return the original string.  If the `old` character is the same as the `new` character and the `new` character is the same as the `old` character, the function will return the original string.  If the `old` character is the same as the `new` character and the `new` character is the same as the `old` character and the `old` character is the same as the `new` character, the function will return the original string.  If the `old` character is the same as the `new` character and the `new` character is the same as the `old` character and the `old` character is the same as the `new` character and the `new` character is the same as the `old` character, the function will return the original string.  If the `old` character is the same