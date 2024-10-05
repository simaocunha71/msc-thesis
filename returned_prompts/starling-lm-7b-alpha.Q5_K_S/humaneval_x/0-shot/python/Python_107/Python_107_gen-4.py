
def even_odd_palindrome(n):
    res_odd = 0
    res_even = 0
    for i in range(1, n+1):
        if i == int(str(i)[::-1]):
            if i % 2 == 0:
                res_even += 1
            else:
                res_odd += 1
    return (res_even, res_odd)

# Time: O(n)
# Space: O(1)


def even_odd_palindrome2(n):
    res_odd = 0
    res_even = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                res_even += 1
            else:
                res_odd += 1
    return (res_even, res_odd)

# Time: O(n)
# Space: O(1)


```



```

```



```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

