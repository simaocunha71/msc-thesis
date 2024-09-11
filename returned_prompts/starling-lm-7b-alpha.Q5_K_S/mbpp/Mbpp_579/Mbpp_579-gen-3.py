"""
def find_dissimilar(t1, t2):
    t1 = set(t1)
    t2 = set(t2)
    dissimilar = t1.symmetric_difference(t2)
    return tuple(dissimilar)


# test
print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))
# (3, 6, 7, 10)
"""

def find_dissimilar(t1, t2):
    t1 = set(t1)
    t2 = set(t2)
    dissimilar = t1 ^ t2
    return tuple(dissimilar)


# test
print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))
# (3, 6, 7, 10)


```
Here, we first convert the two tuples into sets, and then calculate the symmetric difference between the two sets to get a set of dissimilar elements. Finally, we convert the set back to a tuple and return the result.
```

```