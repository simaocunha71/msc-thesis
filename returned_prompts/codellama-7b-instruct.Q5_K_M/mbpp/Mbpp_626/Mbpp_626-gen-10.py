```python
from math import pi, sqrt

def triangle_area(radius):
    if radius < 0:
        return None
    a = 2 * radius
    b = 2 * radius * sqrt(3) / 2
    c = 2 * radius * sqrt(3)
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))
```
