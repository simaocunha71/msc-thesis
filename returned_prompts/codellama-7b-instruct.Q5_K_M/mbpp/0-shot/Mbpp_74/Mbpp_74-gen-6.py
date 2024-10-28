```
def is_samepatterns(patterns,strs):
    return all(s==patterns[i%len(patterns)] for i,s in enumerate(strs))
```
