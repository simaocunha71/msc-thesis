
```python
import re

def text_match_three(text):
    pattern = 'ab{3}'
    if re.search(pattern, text):
        return True
    else:
        return False

print(text_match_three("abbb"))  # True
print(text_match_three("ac"))  # False
```

