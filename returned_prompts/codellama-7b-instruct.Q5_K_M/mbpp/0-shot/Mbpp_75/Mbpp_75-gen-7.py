```
def find_tuples(tuples, k):
    return [t for t in tuples if all(x % k == 0 for x in t)]
```
