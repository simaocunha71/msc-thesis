```
def union_elements(t1, t2):
    return tuple(sorted(set(t1 + t2)))
```



The function `union_elements` takes two tuples `t1` and `t2` as arguments. It first concatenates the two tuples into a single iterable using the `+` operator. Then, it converts this iterable into a set using the `set` function, which removes any duplicate elements. The `sorted` function is then used to sort the elements of the set in ascending order, and the result is converted back into a tuple using the `tuple` function.

The unit test `assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)` ensures that the function works correctly by comparing the result of `union_elements((3, 4, 5, 6),(5, 7, 4, 10))` with the expected output `(3, 4, 5, 6, 7, 10)`. If the function is implemented correctly, this assertion should pass.