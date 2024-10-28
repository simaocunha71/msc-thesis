```python
import re

def find_literals(pattern, literal):
    match = re.search(literal, pattern)
    if match:
        return literal, match.start(), match.end()
    else:
        return None, None, None
```
