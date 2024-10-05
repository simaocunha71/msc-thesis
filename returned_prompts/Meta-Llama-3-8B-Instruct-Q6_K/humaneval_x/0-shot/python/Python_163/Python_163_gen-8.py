```
def generate_integers(a, b):
    if a > b:
        a, b = b, a
    return [i for i in range(a, b+1) if i % 2 == 0]
```

This function first checks if `a` is greater than `b`, and if so, swaps their values. Then, it uses a list comprehension to generate a list of even integers between `a` and `b` (inclusive). The `range(a, b+1)` function generates a sequence of integers from `a` to `b`, and the `if i % 2 == 0` condition filters out the odd integers, leaving only the even ones. The resulting list is then returned.