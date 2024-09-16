```
def validate(n):
    s = str(n)
    for i in range(1, len(s) + 1):
        if s.count(str(i)) > i:
            return False
    return True
```
