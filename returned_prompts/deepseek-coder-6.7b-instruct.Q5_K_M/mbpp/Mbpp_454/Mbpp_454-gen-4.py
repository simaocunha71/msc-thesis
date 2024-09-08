
```python
import re

def text_match_wordz(text):
    pattern = 'z'
    if re.search(pattern,  text):
        return True
    else:
        return False

print(text_match_wordz("pythonz"))
```

