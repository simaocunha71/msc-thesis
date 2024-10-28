```
def find_tuples(tuples, k):
    return [tuple(i for i in t if i % k == 0) for t in tuples]
```
