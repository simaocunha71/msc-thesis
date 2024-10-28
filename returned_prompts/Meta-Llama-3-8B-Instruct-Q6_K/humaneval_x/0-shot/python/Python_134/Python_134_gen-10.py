```
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:  # check if the string is empty
        return False
    last_char = txt[-1]  # get the last character
    if not last_char.isalpha():  # check if the last character is not alphabetical
        return False
    if txt[-2] == ' ':  # check if the last character is not part of a word
        return True
    return False
```


Test the function:
```
print(check_if_last_char_is_a_letter("apple pie"))  # False
print(check_if_last_char_is_a_letter("apple pi e"))  # True
print(check_if_last_char_is_a_letter("apple pi e "))  # False
print(check_if_last_char_is_a_letter(""))  # False
```


This function checks if the last character of the given string is an alphabetical character and is not part of a word. It first checks if the string is empty, and returns False if it is. Then it gets the last character of the string, and checks if it is not alphabetical. If it is not alphabetical, it returns False. If the last character is alphabetical, it checks if the character before it is a space. If it is a space, it means the last character is not part of a word, so it returns True. If the character before it is not a space, it means the last character is part of a word, so it returns False.