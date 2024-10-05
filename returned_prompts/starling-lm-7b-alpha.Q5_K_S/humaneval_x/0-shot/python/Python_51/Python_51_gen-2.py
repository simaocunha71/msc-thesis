Here's a Python function that removes all vowels from a string:

```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(c for c in text if c not in vowels)
```

This function works by iterating over each character in the input string. If the character is not one of the vowels, it is included in the output string. The `join` method is then used to concatenate all the characters in the output string into a single string.

For example, if you call `remove_vowels("abcdef\nghijklm")`, it will remove all vowels from the string, resulting in the string `'bcdf\nghjklm'`. If you call `remove_vowels("aaBAA")`, it will remove all vowels, except for the capital 'B', resulting in the string `'B'`.

The function will also remove all vowels from a string like `'zbcd'`, resulting in the string `'zbcd'`.

Here are some test cases to validate the function:

```python
print(remove_vowels(''))  # ''
print(remove_vowels("abcdef\nghijklm"))  # 'bcdf\nghjklm'
print(remove_vowels('abcdef'))  # 'bcdf'
print(remove_vowels('aaaaa'))  # ''
print(remove_vowels('aaBAA'))  # 'B'
print(remove_vowels('zbcd'))  # 'zbcd'
```

These test cases will output the expected results for the function.

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```