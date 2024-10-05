    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y


# Answer:

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y


# Test:
assert(x_or_y(7, 34, 12) == 34)
assert(x_or_y(15, 8, 5) == 5)

# End of Test


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Test:
# assert(is_prime(7))
# assert(is_prime(15) == False)

# End of Test


# In the name of God

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

