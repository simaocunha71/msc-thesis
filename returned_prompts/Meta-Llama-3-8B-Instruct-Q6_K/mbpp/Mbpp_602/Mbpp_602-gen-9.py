```
def first_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            return char
    return None
```


The function `first_repeated_char(s)` takes a string `s` as input and returns the first repeated character in the string. If no repeated character is found, it returns `None`.

The function works by first creating a dictionary `char_count` to count the occurrence of each character in the string. It then iterates over the dictionary to find the first character with a count greater than 1, which is the first repeated character. If no repeated character is found, it returns `None`.

The unit test `assert first_repeated_char("abcabc") == "a"` ensures that the function correctly returns the first repeated character in the string "abcabc", which is "a".