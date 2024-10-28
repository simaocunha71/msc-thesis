
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n + 1):
        if i == int(str(i)[::-1]):
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd

even, odd = even_odd_palindrome(3)
print(even, odd)  # Output: (1, 2)

even, odd = even_odd_palindrome(12)
print(even, odd)  # Output: (4, 6)



# Time:  O(n)
# Space: O(1)
#
# Definition for a palindrome:
#   - the number is the same as its reverse
#   - e.g. 1, 2, 3, 4, 5, 6, 7, 8, 9
#   - e.g. 11, 22, 33, 44, 55, 66, 77, 88, 99
#
# Definition for an even (odd) number:
#   - the number is divisible by 2 (not divisible by 2)
#   - e.g. 2, 4, 6, 8, ...
#   - e.g. 1, 3, 5, 7, 9, ...
#
# We can use two pointers, left and right, to find palindromes.
# For each palindrome, we check if it's even or odd.
# Then we count the number of even and odd palindromes.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

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