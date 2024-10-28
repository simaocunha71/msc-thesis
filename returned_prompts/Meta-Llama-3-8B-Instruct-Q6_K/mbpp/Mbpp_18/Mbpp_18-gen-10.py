```
def remove_dirty_chars(s1, s2):
    return "".join([c for c in s1 if c not in s2])
```
The problem is asking to create a function that takes two strings as input and returns a new string where all characters from the first string that are present in the second string are removed.

The unit test `assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'` helps to understand the problem better. It shows that the function should return `'bacuve'` when the input strings are `'probasscurve'` and `'pros'`.

To solve this problem, we can use a list comprehension to iterate over each character in the first string. If the character is not present in the second string, we add it to the result list. Finally, we use the `join` method to concatenate the characters in the result list into a string.

For example, if we call `remove_dirty_chars("probasscurve", "pros")`, the function will return `'bacuve'`. This is because the characters `'p'`, `'r'`, and `'o'` are present in both strings, so they are removed from the result. The remaining characters are `'b'`, `'a'`, `'c'`, `'u'`, and `'v'`, which are concatenated into the final string `'bacuve'`.