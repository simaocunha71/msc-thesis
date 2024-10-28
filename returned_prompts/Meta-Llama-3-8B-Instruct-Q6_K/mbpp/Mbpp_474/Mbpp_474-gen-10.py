```
def replace_char(s, old_char, new_char):
    return s.replace(old_char, new_char)
```
This function takes a string `s`, an old character `old_char`, and a new character `new_char` as input. It returns a new string where all occurrences of `old_char` are replaced with `new_char`. The `replace` method of the string class is used to achieve this. 

For example, if we call `replace_char("polygon",'y','l')`, it will return `"pollgon"`. 

This function will work for any string, not just the one provided in the problem description. 

The unit test `assert replace_char("polygon",'y','l')==("pollgon")` ensures that the function works correctly for this specific case. 

The function does not modify the original string, it returns a new string with the replaced characters. This is because strings in Python are immutable, meaning they cannot be changed in place. Instead, a new string is created and returned. 