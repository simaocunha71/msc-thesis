"""
def is_octagonal(n):
    # check if n is a valid octagonal number
    if n < 1:
        return False

    # calculate the nth octagonal number
    octagonal = (8 * n**2) - (8 * n) + 1

    # check if the nth octagonal number is a perfect square
    if octagonal ** 0.5 == int(octagonal ** 0.5):
        return True
    else:
        return False


def nth_octagonal(n):
    # check if n is a valid octagonal number
    if not is_octagonal(n):
        return "Invalid input, please enter a positive integer."

    # calculate the nth octagonal number
    octagonal = (8 * n**2) - (8 * n) + 1

    return octagonal


print(nth_octagonal(5)) # 65
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

```

```