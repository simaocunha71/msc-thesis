```
def first_repeated_char(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            return char
        char_dict[char] = True
    return None
```
The function `first_repeated_char` takes a string `s` as input and returns the first repeated character in the string. It uses a dictionary `char_dict` to keep track of the characters it has seen so far. It iterates over the string, and for each character, it checks if the character is already in the dictionary. If it is, the function returns the character. If not, it adds the character to the dictionary. If the function finishes iterating over the string without finding a repeated character, it returns `None`.

The unit test `assert first_repeated_char("abcabc") == "a"` ensures that the function correctly identifies the first repeated character in the string "abcabc", which is "a". The function should return the first repeated character, not the last one. This means that if there are multiple repeated characters, the function will return the first one it encounters. If there are no repeated characters, the function will return `None`. 