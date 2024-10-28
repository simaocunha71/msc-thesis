```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if len(numbers) == 0:
        return (0, 1)
    else:
        return (sum(numbers), numbers[0])

print(sum_product([]))
print(sum_product([1, 2, 3, 4]))
```