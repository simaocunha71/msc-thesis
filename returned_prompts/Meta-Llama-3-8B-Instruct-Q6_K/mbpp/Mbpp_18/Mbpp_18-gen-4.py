```
def remove_dirty_chars(s, t):
    for char in t:
        s = s.replace(char, '')
    return s
```
This function iterates over each character in the second string, and removes all occurrences of that character from the first string. The result is a new string that does not contain any characters from the second string. This is demonstrated by the unit test `assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'`.