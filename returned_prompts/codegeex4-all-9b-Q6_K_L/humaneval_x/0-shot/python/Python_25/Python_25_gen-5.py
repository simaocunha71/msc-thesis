```python
from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    factor = 2
    while factor * factor <= n:
        while (n % factor) == 0:
            factors.append(factor)
            n //= factor
        factor += 1
    if n > 1:
        factors.append(n)
    return factors
```
