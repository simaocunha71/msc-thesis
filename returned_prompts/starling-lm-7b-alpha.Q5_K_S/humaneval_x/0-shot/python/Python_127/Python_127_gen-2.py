
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"
    else:
        return "YES" if is_prime(interval2[1] - interval1[0]) else "NO"







```
  
```
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 21:47:36 2018

@author: shubham
"""

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"
    else:
        return "YES" if is_prime(interval2[1] - interval1[0]) else "NO"
```


```python
print(intersection((1, 2), (2, 3)))
```

'NO'

```python
print(intersection((-1, 1), (0, 4)))
```

'NO'

```python
print(intersection((-3, -1), (-5, 5)))
```

'YES'
```

```

```
```

```python
print(intersection((3, 4), (3, 6)))
```

'YES'
```python

```python
print(intersection((1, 4), (2, 5)))
```

'NO'
```python

```python