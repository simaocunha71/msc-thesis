def next_power_of_2(n):
    if(n == 0):
        return 1
    else:
        if(n & (n - 1) == 0):
            return n
        else:
            return 2 * next_power_of_2(n & (n - 1))

def test_next_power_of_2():
    assert next_power_of_2(0) == 1
    assert next_power_of_2(3) == 4
    assert next_power_of_2(7) == 8
    assert next_power_of_2(15) == 16
    assert next_power_of_2(17) == 16

test_next_power_of_2()


"""
The function works by repeatedly performing the bitwise AND operation on n and n - 1 until the result becomes 0.
This is because if n is a power of 2, then n & (n - 1) will be 0.
Once the result is 0, the function returns n. Otherwise, it recursively calls itself with the result of the bitwise AND operation and doubles the result each time until it finds the smallest power of 2 greater than or equal to n."""


```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

