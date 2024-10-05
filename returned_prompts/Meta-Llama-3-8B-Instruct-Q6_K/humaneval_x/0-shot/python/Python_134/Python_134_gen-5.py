```
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:  # if the string is empty
        return False
    if txt[-1].isalpha():  # if the last char is an alphabetical character
        if txt[:-1].strip() == "":  # and there is no word before it
            return True
    return False
```


Explanation:
1. We first check if the string is empty, if so, return False.
2. We then check if the last character of the string is an alphabetical character using the `isalpha()` method.
3. If the last character is an alphabetical character, we then check if the rest of the string (excluding the last character) is empty after stripping any leading or trailing spaces. If it is, that means there is no word before it, so we return True.
4. If the above conditions are not met, we return False.