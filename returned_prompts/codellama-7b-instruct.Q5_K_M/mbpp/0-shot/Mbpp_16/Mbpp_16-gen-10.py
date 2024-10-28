```
import re
def text_lowercase_underscore(string):
    pattern = r'^[a-z]+(_[a-z]+)*$'
    return re.match(pattern, string) != None
```
