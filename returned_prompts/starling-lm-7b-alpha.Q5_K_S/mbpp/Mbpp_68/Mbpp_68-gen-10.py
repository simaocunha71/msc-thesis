"""
def is_Monotonic(a):
    if a[0] <= a[1] <= a[2]:
        return True
    elif a[0] >= a[1] >= a[2]:
        return True
    else:
        return False

assert is_Monotonic([6, 5, 4, 4]) == True
"""

def is_Monotonic(a):
    inc = True
    dec = True
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            dec = False
        elif a[i] < a[i+1]:
            inc = False
    if inc == True or dec == True:
        return True
    else:
        return False

assert is_Monotonic([6, 5, 4, 4]) == True

# Code by Sounak, IIESTS
# Stay motivated and keep coding :)

```

1
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