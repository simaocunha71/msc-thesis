```
def union_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    union = set1.union(set2)
    return tuple(sorted(union))
```


The function `union_elements` takes two tuples as input and returns their union in sorted order. It first converts the tuples into sets using the `set` function, which removes duplicates and allows for efficient union operations. The `union` function is then used to combine the two sets, and the result is converted back into a tuple using the `tuple` function. Finally, the `sorted` function is used to sort the elements of the tuple in ascending order before returning it. The unit test `assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)` ensures that the function works correctly.