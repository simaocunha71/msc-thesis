```
def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False

    last_char = txt[-1]
    if not last_char.isalpha():
        return False

    if txt[-2].isspace():
        return True

    return False
```


Explanation:
This function checks if the last character of the input string is an alphabetical character and if it's not a part of a word. 

- It first checks if the string is empty. If it is, it returns False.
- Then it checks if the last character of the string is an alphabetical character. If it's not, it returns False.
- It then checks if the character before the last character is a space. If it is, it means the last character is a part of a word and it returns False.
- If none of the above conditions are met, it returns True, meaning the last character is an alphabetical character and is not a part of a word.