```
import re

def check_str(str_in):
    if re.match(r"[aeiouAEIOU]", str_in):
        return True
    else:
        return False
```
