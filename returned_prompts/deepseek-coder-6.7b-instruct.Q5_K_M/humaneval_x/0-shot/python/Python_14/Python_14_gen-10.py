```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [string[i:] for i in range(len(string))]
```

