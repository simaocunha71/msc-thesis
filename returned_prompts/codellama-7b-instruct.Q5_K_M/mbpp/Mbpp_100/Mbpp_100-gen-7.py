```
def next_smallest_palindrome(n):
    n = str(n)
    n = n[::-1]
    if n > n[::-1]:
        return int(n[::-1]) + 1
    else:
        return int(n[::-1])
```
