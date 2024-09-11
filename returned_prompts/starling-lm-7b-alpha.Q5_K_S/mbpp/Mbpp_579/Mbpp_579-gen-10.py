def find_dissimilar(tuple1, tuple2):
    diss_set = set(tuple1) & set(tuple2)
    return tuple(set(tuple1) - diss_set) + tuple(set(tuple2) - diss_set)


# Test
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)



# Time Complexity: O(n + m), n is the length of tuple1, and m is the length of tuple2
# Space Complexity: O(n + m)
# This is because we need to create two sets to store the elements of two tuples





```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

``