```
def remove_dirty_chars(s, chars):
    for char in chars:
        s = s.replace(char, '')
    return s
```

Explanation:
The function `remove_dirty_chars` takes two parameters: `s` (the first string) and `chars` (the second string). It uses a `for` loop to iterate over each character in the `chars` string. Inside the loop, it uses the `replace` method to remove any occurrences of the current character from the `s` string. Finally, it returns the modified `s` string.

To test the function, the assertion `assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'` is used. This assertion checks if the function correctly removes the characters 'p', 'r', and 'o' from the string "probasscurve" and returns the modified string 'bacuve'.

By running this code, the assertion will pass if the function is implemented correctly, and an error message will be raised if the function fails to remove the specified characters from the string.

Note: The `replace` method in Python returns a new string with all occurrences of the specified character replaced with an empty string. The original string remains unchanged.

```python
def remove_dirty_chars(s, chars):
    for char in chars:
        s = s.replace(char, '')
    return s
```
This function will remove all occurrences of the characters in `chars` from the string `s`.

For example, if you call `remove_dirty_chars("probasscurve", "pros")`, it will return the string `'bacuve'`. This is because the characters 'p', 'r', and 'o' are present in both the original string and the `chars` string, so they are removed from the original string.

The `replace` method in Python is used to replace all occurrences of a specified character with a new character. In this case, it is used to replace the characters in `chars` with an empty string, effectively removing them from the original string.

It's important to note that the `replace` method does not modify the original string, but instead returns a new