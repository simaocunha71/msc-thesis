
def search(lst):
    from collections import Counter
    C = Counter(lst)
    for i in range(len(lst), 0, -1):
        if C[i] >= i:
            return i
    return -1

























# Made By Mostafa_Khaled
```

...
