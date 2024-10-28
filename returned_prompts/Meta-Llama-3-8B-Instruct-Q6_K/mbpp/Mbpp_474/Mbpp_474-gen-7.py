```
def replace_char(s, old, new):
    return s.replace(old, new)
```
This function replaces all occurrences of the character `old` in the string `s` with the character `new`. The `replace` method is a built-in method in Python that replaces a specified phrase with another specified phrase.

For example, if you call `replace_char("polygon",'y','l')`, it will return `"pollgon"`. 

The unit test `assert replace_char("polygon",'y','l')==("pollgon")` confirms this. It checks that the function correctly replaces the character `'y'` with the character `'l'` in the string `"polygon"` to produce the string `"pollgon"`. 