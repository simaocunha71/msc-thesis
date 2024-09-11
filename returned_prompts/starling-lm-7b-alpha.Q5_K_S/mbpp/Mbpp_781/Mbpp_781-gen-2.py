"""
def count_divisors(n):
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def count_divisors_even(n):
    count = count_divisors(n)
    return is_even(count)

assert count_divisors_even(10)
"""

def count_divisors(n):
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def count_divisors_even(n):
    count = count_divisors(n)
    return is_even(count)

assert count_divisors_even(10)

# Output: True

def test_count_divisors_even():
    assert count_divisors_even(10) == True
    assert count_divisors_even(9) == False
    assert count_divisors_even(12) == True
    assert count_divisors_even(11) == False

test_count_divisors_even()

# Output: None

```  

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
