```
def find_dissimilar(t1, t2):
    return tuple([i for i in t1 if i not in t2] + [i for i in t2 if i not in t1])
```







