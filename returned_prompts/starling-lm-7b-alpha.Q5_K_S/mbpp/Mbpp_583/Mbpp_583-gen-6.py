def catalan_number(n):
    if n<1:
        return 0
    elif n==1:
        return 1
    else:
        return catalan_number(n-1) + catalan_number(n-2) * (2*n-3)



"""
assert catalan_number(10)==16796
"""

"""
def catalan_number(n):
    if n<1:
        return 0
    elif n==1:
        return 1
    else:
        return catalan_number(n-1) + catalan_number(n-2) * (2*n-3)
"""






"""
The catalan numbers are given by the recurrence relation
c(n)=sum_{k=0 to n-1} c(k) * c(n-1-k)
with base case c(0)=1
"""


def catalan_number(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return catalan_number(n-1) + catalan_number(n-1) * (2*n-3)

"""
assert catalan_number(10)==16796
"""

```

```
def catalan_number(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return catalan_number(n-1) + catalan_number(n-1) * (2*n-3)
```

```python
def catalan_number(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return catalan_number(n-1) + catalan_number(n-1) * (2*n-3)
```
```
def catalan_number(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return catalan_number(n