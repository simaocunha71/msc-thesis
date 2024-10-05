
def search(lst):
    from collections import Counter
    c = Counter(lst)
    for num in sorted(c):
        if c[num] >= num:
            return num
    return -1


# Alternative solution
from collections import Counter
def search(lst):
    return max(i for i in Counter(lst).keys() if Counter(lst)[i] >= i)


# Another alternative
def search(lst):
    c = Counter(lst)
    return max(i for i, v in c.items() if v >= i)






```
```

```

```

```

```
```

```

```

```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
