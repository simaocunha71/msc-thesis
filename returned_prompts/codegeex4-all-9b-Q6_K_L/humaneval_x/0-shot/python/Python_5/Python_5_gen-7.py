```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [delimeter] + [num for num in numbers] if numbers else []
```

Test the function:
```python
assert intersperse([], 4) == []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
```