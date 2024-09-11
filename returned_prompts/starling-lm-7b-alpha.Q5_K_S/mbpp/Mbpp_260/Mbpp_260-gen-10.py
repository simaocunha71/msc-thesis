"""
def newman_prime(n):
    """Find the nth newman–shanks–williams prime number."""
    if n == 1:
        return 5
    a = 1
    b = 2
    c = 2
    while True:
        a, b = b, (b * b + c) % 10 ** 9 + 7
        if a == 1 and b == c:
            n -= 1
        if not n:
            return c
        c = b
"""

def newman_prime(n):
    """Find the nth newman–shanks–williams prime number."""
    if n == 1:
        return 5
    a = 1
    b = 2
    c = 2
    while True:
        a, b = b, (b * b + c) % (10 ** 9 + 7)
        if a == 1 and b == c:
            n -= 1
        if not n:
            return c
        c = b

# assert newman_prime(3) == 7




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

``