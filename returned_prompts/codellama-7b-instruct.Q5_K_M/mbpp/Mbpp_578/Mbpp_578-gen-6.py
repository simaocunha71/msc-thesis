```
def interleave_lists(lists):
    assert len(lists) > 0
    assert all(len(l) == len(lists[0]) for l in lists)
    return [val for t in zip(*lists) for val in t]
```
