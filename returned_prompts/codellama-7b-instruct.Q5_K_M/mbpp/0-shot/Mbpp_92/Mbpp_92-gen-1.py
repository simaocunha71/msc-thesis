```python
def is_undulating(num):
    s = str(num)
    for i in range(1, len(s)):
        if int(s[i]) > int(s[i-1]):
            continue
        elif int(s[i]) == int(s[i-1]):
            continue
        else:
            return False
    return True
```
