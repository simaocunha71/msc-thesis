```
def replace_char(s, old_char, new_char):
    return s.replace(old_char, new_char)
```

The problem is asking to create a function that replaces a certain character in a given string with a new character. The function should take three parameters: the string, the character to be replaced, and the new character.

The provided unit test `assert replace_char("polygon",'y','l')==("pollgon")` helps to clarify the problem. It shows that the function should replace all occurrences of the character 'y' with 'l' in the string "polygon", resulting in "pollgon".

The solution is a simple Python function using the built-in `replace` method of strings. This method returns a copy of the string where all occurrences of a substring have been replaced with another substring. In this case, we replace all occurrences of the old character with the new character. The function takes three parameters: the string, the old character, and the new character, and returns the modified string. 