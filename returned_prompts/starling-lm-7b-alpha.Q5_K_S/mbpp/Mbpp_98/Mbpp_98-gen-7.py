"""
def multiply_num(nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod / len(nums)
"""

import math

def multiply_num(nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod / len(nums)

assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
# assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)

def test_multiply_num():
    assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)

test_multiply_num()

```
```

```
```

```
```
```