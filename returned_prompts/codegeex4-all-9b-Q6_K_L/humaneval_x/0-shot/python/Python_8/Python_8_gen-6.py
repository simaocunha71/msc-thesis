Here's how you could solve this problem:

```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1
    total_sum = 0
    total_product = 1
    for num in numbers:
        total_sum += num
        total_product *= num
    return total_sum, total_product
```

This function first checks if the list is empty. If it is, it returns a tuple with 0 for the sum and 1 for the product.

If the list is not empty, it initializes `total_sum` to 0 and `total_product` to 1. Then it iterates over each number in the list, adding it to `total_sum` and multiplying `total_product` by it. Finally, it returns a tuple containing `total_sum` and `total_product`.