"""
To solve this problem we need to understand what a centered hexagonal number is. A centered hexagonal number is a hexagonal number where the middle row has a length of one. Here is a sample:

1
2 3 2
3 4 5 4 3
5 6 7 6 5 6
7 8 9 8 7 8
8 9 10 9 8 9
9 10 11 10 11 10
10 11 12 11 12 11 12

To calculate centered hexagonal number for a certain index, we can use the following formula:

def centered_hexagonal_number(n):
    return (n ** 2) + (n // 2 ** 2)

The time complexity of this function is O(1) and the space complexity is O(1).
"""

# Time Complexity: O(1)
# Space Complexity: O(1)

def centered_hexagonal_number(n):
    return (n ** 2) + (n // 2 ** 2)

# Tests
assert centered_hexagonal_number(10) == 271
print("All tests passed.")

```
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
```

```
```
```

```
```
```

```
```
```
```

```
```
```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```