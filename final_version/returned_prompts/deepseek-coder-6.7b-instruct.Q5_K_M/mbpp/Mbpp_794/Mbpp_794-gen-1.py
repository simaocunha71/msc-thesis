```python
import re

def text_starta_endb(text):
    pattern = r'a.*b$'
    if re.search(pattern, text):
        return True
    else:
        return False

print(text_starta_endb("aabbbb")) # True
```

