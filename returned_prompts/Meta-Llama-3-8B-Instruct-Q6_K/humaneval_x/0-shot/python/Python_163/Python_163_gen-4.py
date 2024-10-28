```
def generate_integers(a, b):
    if a > b:
        a, b = b, a

    result = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            result.append(i)

    return result
```

This function first checks if `a` is greater than `b`, and if so, it swaps the two values. It then initializes an empty list `result` to store the even digits between `a` and `b`. It loops through the range from `a` to `b` (inclusive), and for each number, it checks if it is even by using the modulo operator (`%`). If the number is even, it appends it to the `result` list. Finally, it returns the `result` list.

The function works correctly even if `a` is greater than `b`, because it first checks if `a` is greater than `b` and swaps them if necessary. This ensures that the loop iterates over the correct range of numbers. The function also handles the case where `a` and `b` are equal, in which case it simply returns an empty list.