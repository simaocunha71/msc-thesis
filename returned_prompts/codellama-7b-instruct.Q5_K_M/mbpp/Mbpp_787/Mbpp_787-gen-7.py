```
import re

def text_match_three(my_string):
    pattern = r"a[b]{3}"
    return re.search(pattern, my_string)
```
