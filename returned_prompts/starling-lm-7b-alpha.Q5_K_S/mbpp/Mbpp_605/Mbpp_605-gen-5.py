def prime_num(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True



# Another way
def prime_num_v2(num):
    if num<2:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True


```

```
"""
def prime_num(num):
    if num<2:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True
"""
```
```

```
"""
def prime_num(num):
    i = 2
    while i*i <= num:
        if num % i:
            i += 1
        else:
            return False
    return True
"""
```
```python
```

```
"""
def prime_num(num):
    i = 2
    while i*i <= num:
        if num % i:
            i += 1
        else:
            return False
    return True
"""
```
```python
```

```
"""
def prime_num(num):
    sq = int(num**0.5)+1
    for i in range(2,sq):
        if num%i==0:
            return False
    return True
"""
```
```python
```

```
"""
def prime_num(num):
    sq = int(num**0.5)+1
    for i in range(2,sq):
        if num%i==0:
            return False
    return True
"""
```
```python
```

```
"""
def prime_num(