```python
def number_of_substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if s[i:j] != '':
                count += 1
    return count
```