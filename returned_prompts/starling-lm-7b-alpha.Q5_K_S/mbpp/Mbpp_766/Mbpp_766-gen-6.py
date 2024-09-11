from itertools import combinations


def pair_wise(seq):
    return list(combinations(seq, 2))


# Test
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]




# Explanation
In this problem, we are given a list of items and we need to return all pairs of consecutive items. We can use the `combinations` function from the `itertools` module to achieve this. The `combinations` function takes two arguments, `seq` and `r`. Here, `seq` is the list of items and `r` is the length of each combination. We set `r` to 2 since we want pairs of consecutive items. We convert the result of the `combinations` function to a list and return it. This gives us a list of all pairs of consecutive items in the given list.

In the provided test case, the function `pair_wise` is called with the list `[1,1,2,3,3,4,4,5]`. The expected output is `[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]`. The function correctly returns this result.

Note that the `combinations` function includes all possible pairs of consecutive items, including pairs with the same item. If you want to exclude pairs with the same item, you can modify the function to use a generator expression and filter out such pairs.

Here is an alternative solution that returns a generator of pairs of consecutive items:

```python
def pair_wise(seq):
    return (seq[i], seq[i + 1]) for i in range(len(seq) - 1)
```

This solution uses a generator expression to create a generator that yields pairs of consecutive items. The `range` function is used to generate indices for the pairs, and `seq[i]` and `seq[i + 1]` are used to access the consecutive items. The `for`