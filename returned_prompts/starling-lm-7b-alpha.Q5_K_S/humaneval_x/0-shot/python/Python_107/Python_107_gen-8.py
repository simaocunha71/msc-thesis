
def even_odd_palindrome(n):
    e = 0
    o = 0
    for i in range(1,n+1):
        s = str(i)
        if(s == s[::-1]):
            if(i%2==0):
                e += 1
            else:
                o += 1
    return (e,o)


# Driver Program
print(even_odd_palindrome(3))
print(even_odd_palindrome(12))





```
[[[1, 2], [4, 6]]]

```

```

```