```
def extract_even(nested_tuple):
    result = []
    for item in nested_tuple:
        if isinstance(item, tuple):
            result.append(extract_even(item))
        elif item % 2 == 0:
            result.append(item)
    return tuple(result)
```




```
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
```




```
assert extract_even((1, 2, 3, 4, 5, 6)) == (2, 4, 6)
```




```
assert extract_even((1, 2, 3, 4)) == (2, 4)
```




```
assert extract_even((1, 2, 3)) == (2)
```




```
assert extract_even((1, 2)) == (2)
```




```
assert extract_even((1)) == ()
```




```
assert extract_even(()) == ()
```




```
assert extract_even("hello") == ()
```




```
assert extract_even(123) == ()
```




```
assert extract_even([1, 2, 3]) == ()
```




```
assert extract_even({"a": 1, "b": 2}) == ()
```




```
assert extract_even(True) == ()
```




```
assert extract_even(None) == ()
```




```
assert extract_even([1, 2, 3, 4, 5, 6]) == (2, 4, 6)
```




```
assert extract_even((1, 2, 3, 4, 5)) == (2, 4)
```




```
assert extract_even([1, 2, 3, 4, 5]) == ()
```




```
assert extract_even({1, 2, 3, 4}) == ()
```




```
assert extract_even({1: 1, 2: 2}) == ()
```




```
assert extract_even(set([1, 2, 3])) == ()
```




```
assert extract_even(frozenset([1, 2, 3])) == ()
```




```
assert extract_even({1, 2, 3, 4, 5, 6}) == ()
```




``