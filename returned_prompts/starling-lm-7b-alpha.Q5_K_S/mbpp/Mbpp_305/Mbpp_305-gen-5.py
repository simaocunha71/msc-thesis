def start_withp(words):
    p = []
    for i in words:
        if i[0] == 'p':
            p.append(i)
    return p[0],p[1]


# Another way:
def start_withp(words):
    p = [i for i in words if i[0] == 'p']
    if len(p) >= 2:
        return p[0],p[1]
    else:
        return None,None

# Test
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

# Test 2:
assert start_withp(["Python", "Java", "c"])==None

# Test 3:
assert start_withp(["Python", "c"])==None

# Test 4:
assert start_withp(["Python"])==None


# Python3 Version
# Python3 Version
# Python3 Version
# Python3 Version

# Python3 Version
# Python3 Version

```

```
def start_withp(words):
    p = []
    for i in words:
        if i[0] == 'p':
            p.append(i)
    return p[0],p[1]
```
```

def start_withp(words):
    p = [i for i in words if i[0] == 'p']
    if len(p) >= 2:
        return p[0],p[1]
    else:
        return None,None
```
```python
# Python3 Version
# Python3 Version
# Python3 Version
# Python3 Version

# Python3 Version
# Python3 Version

```
```python
"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""

def start_withp(words):
    p = []
    for i in words:
        if i[0] == 'p':
            p