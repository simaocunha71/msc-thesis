```
import re

def is_decimal(str):
    return re.match(r'^[0-9]+.[0-9][0-9]$', str)
```

