def capital_words_spaces(s):
    res = ""
    for c in s:
        if c.isupper():
            res += " " + c
        else:
            res += c
    return res

def test_capital_words_spaces():
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("JavaScript") == 'JavaScript'
    assert capital_words_spaces("C++") == 'C++'

test_capital_words_spaces()


"""
This function works by iterating over each character in the given string and checking if it is uppercase. If it is, then the function appends a space followed by the uppercase character to the result string. If it is not, then the function simply appends the character to the result string. Finally, the function returns the result string.

The function asserts that the result of calling the function with the example inputs "Python", "JavaScript", and "C++" matches the expected outputs. This helps to ensure that the function is working correctly.
"""

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

``