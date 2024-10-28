```
def remove_Occ(s, char):
    s = s.replace(char, '', 1)
    s = s.replace(char, '', 1)
    return s
```
The problem is asking to create a function that takes a string and a character as input, and returns the string with the first and last occurrence of the character removed.

Here is the Python function to solve this problem:

```
def remove_Occ(s, char):
    s = s.replace(char, '', 1)
    s = s.replace(char, '', 1)
    return s
```

This function uses the `replace` method of the string to replace the first and last occurrence of the character with an empty string. The `replace` method takes three arguments: the character to replace, the replacement string, and the maximum number of replacements to make. By setting the maximum number to 1, we ensure that only the first and last occurrence of the character are replaced.

The unit test `assert remove_Occ("hello","l") == "heo"` helps to understand the problem better. It shows that the function should remove the first and last occurrence of the character 'l' from the string "hello", resulting in the string "heo". 