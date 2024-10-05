
def pluck(arr):
    if len(arr) == 0:
        return []
    evens = [i for i in arr if i % 2 == 0]
    if len(evens) == 0:
        return []
    return [min(evens, key=lambda x: x[1])]

```

```
