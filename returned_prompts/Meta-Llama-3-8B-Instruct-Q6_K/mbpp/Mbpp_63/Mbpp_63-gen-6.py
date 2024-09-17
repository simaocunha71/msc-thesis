You can solve this problem by comparing each pair of numbers in the tuple list and finding the maximum difference.

Here is the Python function that does this:
```
def max_difference(tuples):
    return max(abs(a - b) for a, b in tuples)
```
This function uses a generator expression to calculate the absolute difference for each pair of numbers in the tuple list, and then returns the maximum of these differences. The `abs` function is used to ensure that the difference is always positive, regardless of whether the pair is in ascending or descending order.

For example, if you call the function with the following tuple list:
```
[(3, 5), (1, 7), (10, 3), (1, 2)]
```
The function will return `7`, which is the maximum difference between the pairs `(1, 2)` and `(10, 3)`. This is consistent with the unit test:
```
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
```  # passes
```
```

