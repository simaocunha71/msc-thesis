```
import re
def extract_quotation(str):
    return re.findall(r'"(.*?)"', str)
```
