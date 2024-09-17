```
def union_elements(t1, t2):
    return tuple(sorted(set(t1 + t2)))
```
This function works by concatenating the two input tuples, then converting the result to a set (which removes duplicates), and finally converting the set back to a tuple and sorting it. The sorted() function is used to ensure that the output is in ascending order. The unit test provided ensures that the function works correctly. For example, the test `assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)` checks that the function correctly finds the union of the elements in the two tuples and returns them in sorted order. 