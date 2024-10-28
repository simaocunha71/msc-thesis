```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    else:
        return [numbers[0]] + [delimeter] + intersperse(numbers[1:], delimeter)
```
