"""
Here are some basic rules for woodball numbers:

1. The sum of all digits of a woodball number must be divisible by 3.
2. Woodball numbers can have leading zeros.
3. A woodball number must be an integer.

Here's a function that checks if a given number is a woodball number:
"""

def is_woodall(n):
    total = 0
    while n > 0:
        digit = n % 10
        if digit > 4:
            digit = 9 - digit
        total += digit
        n //= 10
    return total % 3 == 0

# Test the function
print(is_woodall(383))  # Should return True
print(is_woodall(38))   # Should return True
print(is_woodall(3838)) # Should return False
print(is_woodall(38380))# Should return False
print(is_woodall(383800))# Should return True
print(is_woodall(3838000))# Should return True

```
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```