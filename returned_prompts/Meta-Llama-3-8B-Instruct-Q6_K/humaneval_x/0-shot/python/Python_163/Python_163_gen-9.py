
The `generate_integers` function takes two positive integers `a` and `b` as input and returns a list of even integers between `a` and `b` (inclusive), in ascending order.

Here's the solution:

```
def generate_integers(a, b):
    if a > b:
        a, b = b, a
    return [i for i in range(a, b+1) if i % 2 == 0]
```

Explanation:

1. If `a` is greater than `b`, we swap them to ensure that `a` is always less than or equal to `b`.
2. We use a list comprehension to generate the even integers between `a` and `b`.
3. The condition `i % 2 == 0` checks whether the integer `i` is even. If it is, it is included in the list.

Example outputs:

```
generate_integers(2, 8) => [2, 4, 6, 8]
generate_integers