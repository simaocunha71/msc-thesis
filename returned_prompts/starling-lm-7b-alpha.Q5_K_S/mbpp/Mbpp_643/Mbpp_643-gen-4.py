"""
def text_match_wordz_middle(text):
    for c in text:
        if c == 'z' and (text.startswith('z') or text.endswith('z')):
            return False
    return True
"""

text_match_wordz_middle = lambda text: 'z' in text and (text.startswith('z') or text.endswith('z')) == False

def test_function():
    assert text_match_wordz_middle("pythonzabc.") == True
    assert text_match_wordz_middle("zpythonzabc.") == False
    assert text_match_wordz_middle("abc.pythonz") == True
    assert text_match_wordz_middle("zabc.pythonz") == False

test_function()
#
"""
"""

```

```
"""
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

