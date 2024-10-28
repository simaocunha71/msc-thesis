```
def replace_specialchar(s):
    s = s.replace(" ", ":")
    s = s.replace(",", ":")
    s = s.replace(".", ":")
    return s
```


The function takes a string as an argument and replaces all occurrences of spaces, commas, and dots with a colon. It uses the `replace` method of the string to achieve this. The `replace` method takes two arguments: the first is the substring to replace, and the second is the replacement string. In this case, the replacement string is a colon. The function returns the modified string. 

The unit test provided ensures that the function works correctly. It checks that the function replaces all occurrences of spaces, commas, and dots with a colon in the given string. 

Note that this function is case-sensitive and does not preserve the original case of the characters. If you want to preserve the original case, you can use a list comprehension with the `replace` method and the `join` method to create a new string. Here's an example:
```
def replace_specialchar(s):
    return ":".join(c if c.isalnum() else ":" for c in s)
```


This function uses a list comprehension to iterate over each character in the string. If the character is alphanumeric (i.e., a letter or a number), it is left unchanged. If the character is not alphanumeric, it is replaced with a colon. The `join` method is then used to concatenate the characters into a new string. This function preserves the original case of the characters. 