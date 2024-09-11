"""
def text_lowercase_underscore(s):
    return True if s.isalpha() and '_' in s else False
"""

def text_lowercase_underscore(s):
    return True if s.islower() and '_' in s else False



def test_text_lowercase_underscore():
    assert text_lowercase_underscore("aab_cbbbc") == True
    assert text_lowercase_underscore("aab_cbb_dcc") == True
    assert text_lowercase_underscore("abc_def") == False
    assert text_lowercase_underscore("abC_def") == False
    assert text_lowercase_underscore("abcd_efgh") == False
    assert text_lowercase_underscore("aab_cbbbc") == True
    assert text_lowercase_underscore("abc_defg") == False
    assert text_lowercase_underscore("abcd_efghi") == False

test_text_lowercase_underscore()





























































```

```

```python

```

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python