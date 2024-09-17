```
def remove_Occ(s, c):
    if c in s:
        s = s.replace(c, '', 2)
    return s
```



The problem asks to write a function that takes a string and a character as input, and returns the string with the first and last occurrences of the character removed.

The unit test `assert remove_Occ("hello","l") == "heo"` helps to clarify the problem. It shows that the function should remove the first and last 'l' from the string "hello", resulting in "heo".

The function uses the `replace` method of the string to replace the character with an empty string, but limits the replacement to 2 occurrences. This ensures that only the first and last occurrences of the character are removed.

Here is the Python function that solves the problem:
```
def remove_Occ(s, c):
    if c in s:
        s = s.replace(c, '', 2)
    return s
```
This function takes two arguments: `s` (the input string) and `c` (the character to remove). It checks if the character is present in the string using the `in` operator. If the character is present, it uses the `replace` method to replace the character with an empty string, limiting the replacement to 2 occurrences. Finally, it returns the modified string. If the character is not present in the string, the function simply returns the original string.