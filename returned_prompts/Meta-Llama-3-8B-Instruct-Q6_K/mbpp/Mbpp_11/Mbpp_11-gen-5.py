```
def remove_Occ(s, char):
    if char not in s:
        return s
    else:
        return s.replace(char, '', 2)
```





Note: This function uses the replace method of the string to remove the first and last occurrence of the given character. The replace method takes three arguments: the character to be replaced, the replacement character, and the maximum number of replacements to be done. In this case, we set the maximum number of replacements to 2, so it replaces the first and last occurrence of the character. If the character is not found in the string, the function returns the original string.