
```python
import re
def text_match_wordz(text):
    patterns = 'z'
    if re.search(patterns,  text):
        return True
    else:
        return False

print(text_match_wordz("pythonz."))
```

