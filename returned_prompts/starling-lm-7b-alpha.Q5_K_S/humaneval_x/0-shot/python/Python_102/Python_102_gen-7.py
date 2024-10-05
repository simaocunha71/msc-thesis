
def choose_num(x, y):
    if x <= 0 or y <= 0:
        return -1
    elif x % 2 == 0:
        return x
    elif y % 2 == 0:
        return y
    else:
        return max(x, y) - 1

choose_num(12, 15)  # return: 14
choose_num(13, 12)  # return: -1



# Other Solutions:

def choose_num(x, y):
    if x == y:
        return x if x % 2 == 0 else -1
    else:
        return -1 if (y - x) % 2 == 1 else max(x, y)

def choose_num(x, y):
    if x % 2 == 0:
        return x
    elif y % 2 == 0:
        return y
    else:
        return max(x, y) - 1

def choose_num(x, y):
    if x % 2 == 0:
        return x
    elif y % 2 == 0:
        return y
    else:
        if (y - x) % 2 == 1:
            return -1
        else:
            return max(x, y)



```

```python
def choose_num(x, y):
    if x == y and x % 2 == 0:
        return x
    elif x == y and x % 2 != 0:
        return -1
    elif x < y and x % 2 == 0:
        return x
    elif x < y and x % 2 != 0:
        return -1
    elif x > y and y % 2 == 0:
        return y
    elif x > y and y % 2 != 0:
        return -1
    else:
        return max(x, y) - 1
```
```python
def choose_num(x, y):
    if x % 2 == 0:
        return x
    elif y % 2 ==