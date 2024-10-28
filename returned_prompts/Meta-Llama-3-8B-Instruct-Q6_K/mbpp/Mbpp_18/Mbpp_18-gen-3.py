```
def remove_dirty_chars(s1, s2):
    return ''.join([c for c in s1 if c not in s2])
```





The problem is asking to create a function that takes two strings as input and returns a new string where all characters from the first string that are present in the second string are removed.

The unit test `assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'` helps to understand the problem better. It suggests that the function should remove all characters from the string "probasscurve" that are present in the string "pros", resulting in the string "bacuve".

Here is the Python solution for the problem:
```
def remove_dirty_chars(s1, s2):
    return ''.join([c for c in s1 if c not in s2])
```
This function uses a list comprehension to iterate over each character `c` in the first string `s1`. It checks if `c` is not in the second string `s2` using the `not in` operator. If `c` is not in `s2`, it includes `c` in the new string. The `join` method is then used to concatenate all the characters in the list into a single string.