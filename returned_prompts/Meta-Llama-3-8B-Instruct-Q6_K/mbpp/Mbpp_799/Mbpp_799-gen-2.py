```
def left_rotate(n, d):
    d = d % 32
    return ((n << d) | (n >> (32 - d)))
```
This function takes two arguments, `n` and `d`. It first calculates the remainder of `d` divided by 32, because shifting by 32 bits or more is the same as shifting by 0 bits. Then it shifts the bits of `n` to the left by `d` bits, and then shifts the bits to the right by `32 - d` bits. The bitwise OR operator `|` is used to combine the two results. The result is the number with its bits rotated to the left by `d` bits. 