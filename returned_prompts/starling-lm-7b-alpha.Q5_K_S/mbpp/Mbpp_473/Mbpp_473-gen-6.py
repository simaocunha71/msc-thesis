Here is one way to solve this problem:

```python
def tuple_intersection(*args):
    first_tuple = args[0]
    result = {first_tuple[i] for i in range(len(first_tuple))}
    for tuple_ in args[1:]:
        for elem in tuple_:
            if elem in result:
                result.add(elem)
    return result
```

This function works by first taking the first tuple and creating a set of its elements. It then compares the set of the first tuple to each of the other tuples. If an element is found in the result set and also in one of the other tuples, it is added to the result set.

The time complexity of this solution is O(n + m), where n and m are the lengths of the first and second tuple respectively.

To test the function, you can use the following code:

```python
from frozendict import frozenset  # Required to create a frozenset

def test_tuple_intersection():
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == frozenset({(4, 5), (3, 4), (5, 6)})

test_tuple_intersection()
```

This test case checks if the function correctly returns the intersection of the tuples, ignoring their order. The assertion in the `test_tuple_intersection` function ensures that the function's result matches the expected result.

Note that the `frozenset` function is used to create a frozenset from the result set, which is necessary because sets are not hashable and cannot be used as dictionary keys.

```

```

```python
def tuple_intersection(*args):
    first_tuple = args[0]
    result = {first_tuple[i] for i in range(len(first_tuple))}
    for tuple_ in args[1:]:
        for elem in tuple_:
            if elem in result:
                result