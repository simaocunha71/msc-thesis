
```python
from itertools import product

def combinations_colors(lst, n):
    return list(product(*([lst]*n)))

print(combinations_colors(["Red","Green","Blue"],1))
```

