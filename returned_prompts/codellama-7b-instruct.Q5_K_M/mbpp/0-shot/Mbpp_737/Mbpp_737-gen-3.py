```
import re

def check_str(str):
    pattern = re.compile(r"^[aeiouAEIOU]")
    return pattern.match(str)
```
