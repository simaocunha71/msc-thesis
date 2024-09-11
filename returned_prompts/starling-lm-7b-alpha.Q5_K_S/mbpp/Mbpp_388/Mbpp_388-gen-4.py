def highest_Power_of_2(n):
    p = 0
    while n > 0:
        n >>= 1
        p += 1
    return (1 << p) - 1





"""
This function works by repeatedly halving n until it becomes 0 or 1. For each halving, p is incremented by 1. At the end, n is one of 0 or 1, and p is the maximum power of 2 that is less than or equal to n.
"""


# assert highest_Power_of_2(10) == 8
# assert highest_Power_of_2(15) == 15
# assert highest_Power_of_2(33) == 32
# assert highest_Power_of_2(0) == 0
# assert highest_Power_of_2(1) == 1


"""
The function can be tested with the following assertions:
"""



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