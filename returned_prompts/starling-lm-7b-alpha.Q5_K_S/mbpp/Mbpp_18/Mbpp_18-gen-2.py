```
def remove_dirty_chars(s1, s2):
    for c in s2:
        s1 = s1.replace(c, "")
    return s1
```

Explanation:

To solve this problem, we can define a function called `remove_dirty_chars` that takes two strings as input: `s1` and `s2`. Inside the function, we iterate over each character in `s2` and use the `replace` method to remove that character from `s1`. Finally, we return the modified `s1`.

In the given assertion, the function is tested with the strings "probasscurve" and "pros". The expected output is "bacuve". This means that the characters 'p', 'o', 'b', and 'a' are removed from the original string.

To use this function, you can simply call it and pass the appropriate strings as arguments. For example:

```python
result = remove_dirty_chars("probasscurve", "pros")
print(result)  # Output: "bacuve"
```

This will remove the characters 'p', 'o', and 'b' from the string "probasscurve" and return the modified string "bacuve".

Note that the `replace` method in Python returns a new string with the specified character replaced. It does not modify the original string. Therefore, we need to assign the result of `s1.replace(c, "")` back to `s1` in order to update its value.

It's important to note that this solution is case-sensitive. If you want a case-insensitive version, you can convert both `s1` and `s2` to lowercase or uppercase before performing the replacements.

```python
def remove_dirty_chars(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    for c in s2:
        s1 = s1.replace(c, "")
    return s1
```

This will ensure that characters like 'P', 'O', and 'B' are also removed from the original string.

Overall, the solution provided is a simple and effective way to remove characters