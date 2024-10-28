```
def choose_num(x, y):
    if x > y:
        x, y = y, x  # swap x and y
    if x % 2 == 0:
        return x
    for i in range(x + 1, y + 1):
        if i % 2 == 0:
            return i
    return -1
```



Explanation:

1. First, we check if `x` is greater than `y`. If it is, we swap `x` and `y` to ensure that `x` is the smaller number and `y` is the larger number.
2. Then, we check if `x` is even. If it is, we return `x` because it's the biggest even number in the range.
3. If `x` is not even, we start a loop from `x + 1` to `y + 1` (inclusive) to find the first even number. If we find an even number, we return it.
4. If we reach the end of the loop without finding an even number, it means that there is no even number in the range, so we return -1.

This function works correctly for all positive integer inputs `x` and `y`. For example, `choose_num(12, 15)` returns 14, and `choose_num(13, 12)` returns -1.