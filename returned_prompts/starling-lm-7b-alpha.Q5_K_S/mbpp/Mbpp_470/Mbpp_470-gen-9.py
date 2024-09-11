def add_pairwise(tup):
    res = []
    for i in range(len(tup)-1):
        res.append(tup[i]+tup[i+1])
    res.append(tup[-1]+tup[-2])
    return tuple(res)

# assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)

def add_pairwise(tup):
    res = []
    for i in range(len(tup)-1):
        res.append(tup[i]+tup[i+1])
    res.append(tup[-1]+tup[-2])
    return tuple(res)

assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)

# Code by Siddharth Ostawal

def add_pairwise(tup):
    res = []
    for i in range(len(tup)-1):
        res.append(tup[i]+tup[i+1])
    res.append(tup[-1]+tup[-2])
    return tuple(res)

assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)

# Code by Siddharth Ostawal
"""
"""

def add_pairwise(tup):
    res = []
    for i in range(len(tup)-1):
        res.append(tup[i]+tup[i+1])
    res.append(tup[-1]+tup[-2])
    return tuple(res)

assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)

# Code by Siddharth Ostawal

```
  
The above code defines a function `add_pairwise` that takes a tuple as an input and returns a tuple with the pair