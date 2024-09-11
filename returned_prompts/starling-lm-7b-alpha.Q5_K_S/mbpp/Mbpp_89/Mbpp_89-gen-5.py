```
def closest_num(n):
    # Initialize minimum number
    min_num = float("inf")

    # Traverse the range from 1 to n
    for i in range(1, n + 1):
        if i < n and i < min_num:
            min_num = i

    return min_num
```

This Python function `closest_num` takes a number `n` as input and returns the closest smaller number. It initializes a variable `min_num` with the maximum possible value (`float("inf")`). Then, it traverses the range from 1 to