```python
def next_smallest_palindrome(x):
    s = str(x)
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            s = s[:i] + s[-i-1] + s[i+1:]
            break
    else:
        s = str(int(s) + 1)
    return int(s)
```