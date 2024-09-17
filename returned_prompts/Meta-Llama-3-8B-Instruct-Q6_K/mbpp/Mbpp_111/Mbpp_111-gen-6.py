```
def common_in_nested_lists(nested_lists):
    return set.intersection(*map(set, nested_lists))
```



The problem is asking to find the common elements in the given nested lists. The unit test provided suggests that the function should return a set of common elements.

The solution uses the built-in Python functions set and map to convert the nested lists to sets and then find the intersection of these sets. The function * operator is used to unpack the map function's result into separate arguments for the set.intersection function.

Here is the unit test:

```
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
```



This test checks if the function returns the expected set of common elements. The expected result is a set containing the elements 18 and 12, which are common to all the lists in the input. The actual result should also be the same set for the test to pass.