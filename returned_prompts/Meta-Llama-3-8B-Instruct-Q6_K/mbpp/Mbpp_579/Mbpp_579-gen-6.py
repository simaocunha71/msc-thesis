You can use a list comprehension to find the dissimilar elements in the given two tuples. The function should iterate over the elements of both tuples, and if an element is not present in the other tuple, it should be added to the result.

Here is the Python function that solves the problem:

```
def find_dissimilar(t1, t2):
    return tuple(set(t1) ^ set(t2))
```

This function uses the built-in `set` function to convert the tuples into sets. The `^` operator is used to find the symmetric difference of the two sets, which are the elements that are present in exactly one of the sets. The `tuple` function is used to convert the result back into a tuple.

The unit test `assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)` passes with this function. It correctly identifies the dissimilar elements as (3, 6, 7, 10) and returns them as a tuple. 