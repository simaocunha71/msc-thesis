```python
import re

def extract_quotation(string):
    return re.findall(r'"([^"]*)"', string)
```
