from typing import List, Tuple
def min_product_tuple(lst: List[Tuple[int, int]]) -> int:
    min_product = float("inf")
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            min_product = min(min_product, lst[i][0] * lst[i][1] * lst[j][0] * lst[j][1])
    return min_product


# Test Cases
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
assert min_product_tuple([(3, 4), (2, 6), (5, 8)]) == 48
assert min_product_tuple([(1, 2), (3, 4), (5, 6)]) == 2




"""

Minimum product can be found by multiplying the smallest value from each tuple.
"""

































```

```

```

```python

```

```

```python

```python

```

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python

```python
```python

```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
