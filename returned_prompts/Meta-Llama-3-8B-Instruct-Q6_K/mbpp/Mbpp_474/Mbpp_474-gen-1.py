```
def replace_char(s, old, new):
    return s.replace(old, new)
```
This function takes three parameters: the string `s`, and the characters `old` and `new`. It returns a new string where all occurrences of `old` in `s` are replaced with `new`. The unit test provided ensures that the function works correctly. For example, `replace_char("polygon",'y','l')` should return `"pollgon"`. 

The `replace` method of the string class in Python is used to replace all occurrences of a substring with another substring. It takes two parameters: the substring to be replaced and the new substring. The method returns a new string where all occurrences of the old substring are replaced with the new substring. 

In this function, `s.replace(old, new)` is used to replace all occurrences of `old` in `s` with `new`. The result is then returned as the output of the function. 

This function does not modify the original string, but returns a new string with the replaced characters. If you want to modify the original string, you can use the `s = s.replace(old, new)` statement instead. 

This function is case sensitive, so if you want to make it case insensitive, you can convert both `s` and `old` to lower case or upper case before replacing the characters. For example, `s = s.lower().replace(old.lower(), new.lower())`. 

This function also replaces all occurrences of `old` in `s`, not just the first one. If you want to replace only the first occurrence of `old` in `s`, you can use the `s = s.replace(old, new, 1)` statement. 

This function does not handle situations where `old` is not found in `s`. If you want to handle this situation, you can add a condition to check if `old` is found in `s` before replacing the characters. For example, `if old in s: s = s.replace(old, new)`. 

This function assumes that `old` and `new` are strings. If `old` or `new` can be other types, you may need to add error checking code to handle this. 

This function does not handle situations where `s` is `None`. If you want to handle this situation, you can add a condition to check if `s` is `None` before trying to replace the characters. For example, `if s