```
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
```



The provided unit test `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]` suggests that the function should return a list of tuples where all elements are divisible by k.

The function uses a list comprehension to iterate over the input list of tuples. For each tuple, it checks if all elements are divisible by k using the `all` function and a generator expression. The `all` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. The generator expression `i % k == 0 for i in t` checks if each element `i` in the tuple `t` is divisible by `k` (i.e., if `i % k` is equal to 0). If the tuple passes this test, it is included in the output list.

Here's the solution:
```
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
```



The unit test `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]` passes for this solution. It correctly returns the tuple `(6, 24, 12)` because all its elements (6, 24, and 12) are divisible by 6. The other tuples `(7, 9, 6)` and `(12, 18, 21)` do not meet this condition, so they are not included in the output.