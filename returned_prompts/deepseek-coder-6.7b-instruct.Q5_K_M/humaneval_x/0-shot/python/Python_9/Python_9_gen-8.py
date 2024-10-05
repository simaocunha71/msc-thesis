Here is the solution:

```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    max_num = numbers[0]
    result = [max_num]

    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        result.append(