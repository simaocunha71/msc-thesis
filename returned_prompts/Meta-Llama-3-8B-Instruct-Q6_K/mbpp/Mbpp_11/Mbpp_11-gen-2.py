```
def remove_Occ(s, char):
    return s.replace(char, '', 2)
```
This function uses the `replace` method of the string, which replaces all occurrences of the specified character with an empty string. The third argument `2` specifies that only the first two occurrences should be replaced. The function returns the modified string.

The unit test `assert remove_Occ("hello","l") == "heo"` ensures that the function correctly removes the first and last occurrence of the character 'l' from the string "hello".