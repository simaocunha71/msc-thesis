```
import re

def check_str(my_str):
    pattern = re.compile(r"^[aeiou]")
    return bool(pattern.match(my_str))
```
