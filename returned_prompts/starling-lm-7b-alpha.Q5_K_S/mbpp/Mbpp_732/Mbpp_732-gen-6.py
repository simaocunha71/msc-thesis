```
def replace_specialchar(s):
    s = s.replace(" ", ":")
    s = s.replace(",", ":")
    s = s.replace(".", ":")
    return s
```

Here is a function that replaces all occurrences of spaces, commas, and dots with a colon in a string:

```python
def replace_specialchar(s):
    s = s.replace(" ", ":")
    s = s.replace(",", ":")
    s = s.replace(".", ":")
    return s
```

The function takes a string `s` as input and uses the `replace()` method to replace all occurrences of spaces, commas, and dots with a colon. The modified string is then returned as the output of the function. 

In the provided `assert` statement, the function is tested with the string `'Python language, Programming language.'`. The expected output of the function for this input is `'Python:language::Programming:language:'`. 

By using the `replace()` method with the appropriate characters as arguments, the function effectively replaces all occurrences of spaces, commas, and dots with a colon in the given string.

```python
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
```

The assert statement asserts that the function `replace_specialchar` correctly replaces all special characters with a colon in the given string, and verifies that the output matches the expected result.
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
