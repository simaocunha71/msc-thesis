```python
def combinations_list(lst):
    def rec(lst, accum, i):
        if i == len(lst):
            return [accum]
        else:
            return rec(lst, accum + [lst[i]], i + 1) + rec(lst, accum, i + 1)
    return rec(lst, [], 0)
```
