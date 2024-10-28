```
def find_tuples(lst, k):
    return [t for t in lst if all(x % k == 0 for x in t)]
```
The function `find_tuples` takes a list of tuples `lst` and an integer `k` as input. It returns a list of tuples where all elements are divisible by `k`.

The `all` function is used with a generator expression to check if all elements in each tuple are divisible by `k`. If all elements in a tuple are divisible by `k`, the tuple is included in the output list.

The unit test `assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]` ensures that the function works correctly. It checks that the tuple `(6, 24, 12)` is the only tuple in the input list where all elements are divisible by `6`, and that the function returns this tuple as expected.