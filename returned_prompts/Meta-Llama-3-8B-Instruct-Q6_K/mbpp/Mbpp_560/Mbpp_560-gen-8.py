```
def union_elements(t1, t2):
    return tuple(sorted(set(t1 + t2)))
```
The problem asks you to create a function that takes two tuples as input, finds the union of their elements (i.e., removes duplicates), and returns the result in sorted order.

Here's the solution:

We use the `set` data structure to find the union of the elements. The `set` data structure automatically removes duplicates. We then convert the `set` back to a tuple using the `tuple` function. Finally, we sort the tuple using the `sorted` function and return the result.

The unit test `assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)` ensures that the function works correctly. It checks that the function returns the expected result when given two tuples as input. If the function returns the correct result, the unit test passes; otherwise, it fails.