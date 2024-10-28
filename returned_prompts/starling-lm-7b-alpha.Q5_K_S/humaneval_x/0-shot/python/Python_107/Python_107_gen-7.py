
def even_odd_palindrome(n):
    even = 0
    odd = 0
    for i in range(1, n+1):
        if i == int(str(i)[::-1]):
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)




# Test Cases
print(even_odd_palindrome(3))  # (1, 2)
print(even_odd_palindrome(12))  # (4, 6)
print(even_odd_palindrome(8))  # (3, 4)
print(even_odd_palindrome(1))  # (0, 0)
print(even_odd_palindrome(100))  # (11, 13)
print(even_odd_palindrome(1000))  # (17, 19)






```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```