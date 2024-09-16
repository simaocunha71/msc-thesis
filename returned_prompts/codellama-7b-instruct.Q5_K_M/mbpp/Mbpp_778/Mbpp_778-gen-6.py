```
def pack_consecutive_duplicates(lst):
    return list(
        itertools.groupby(
            lst,
            key=lambda x: x,
            # this is what groups consecutive duplicates together
            # i.e. the difference between consecutive elements is 1
            # https://docs.python.org/3/library/itertools.html#itertools.groupby
            lambda x, y: y - x,
        )
    )
```