
def even_odd_palindrome(n):
    evens = 0
    odds = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                evens += 1
            else:
                odds += 1
    return (evens, odds)

# Time:  O(n)
# Space: O(1)

# Test Cases
print(even_odd_palindrome(3))  # [1, 2]
print(even_odd_palindrome(12))  # [4, 6]

















































```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

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