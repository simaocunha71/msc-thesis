```python
import re

def is_decimal(num_str):
    return re.match(r'^[0-9]+\.[0-9]{2}$', num_str)
```
