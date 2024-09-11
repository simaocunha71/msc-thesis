"""
def toggle_middle_bits(n):
    b = bin(n)[2:]
    if len(b) == 1:
        return n + 1
    return int(b[:-2], 2) + int(b[-1], 2) * 2 + (int(b[-2], 2) + 1) * 2**(len(b) - 2)

# Python3 program to demonstrate
# the above approach

# Driver program to test the above
# function
print(toggle_middle_bits(9))
"""

def toggle_middle_bits(n):
    b = bin(n)[2:]
    if len(b) == 1:
        return n + 1
    return int(b[:-2], 2) + int(b[-1], 2) * 2 + (int(b[-2], 2) + 1) * 2**(len(b) - 2)

# Python3 program to demonstrate
# the above approach

# Driver program to test the above
# function
print(toggle_middle_bits(9))











































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