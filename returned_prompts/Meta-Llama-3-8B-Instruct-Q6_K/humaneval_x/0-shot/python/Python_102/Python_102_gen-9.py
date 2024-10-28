```
def choose_num(x, y):
    if x % 2 == 0:
        start = x
    else:
        start = x + 1
    if y % 2 == 0:
        end = y
    else:
        end = y - 1
    if start <= end:
        return start
    else:
        return -1
```



