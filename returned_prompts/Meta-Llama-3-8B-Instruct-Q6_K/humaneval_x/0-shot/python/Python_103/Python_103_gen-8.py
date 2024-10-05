```
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round((n + m) / 2)
    return bin(avg)[2:]
```

The function `rounded_avg(n, m)` takes two positive integers `n` and `m` as input. It first checks if `n` is greater than `m`. If it is, the function returns -1.

If `n` is not greater than `m`, the function calculates the average of the integers from `n` through `m` by adding `n` and `m` and then dividing by 2. It then rounds the average to the nearest integer using the `round` function.

Finally, the function converts the rounded average to binary using the `bin` function and returns the result. Note that the `[2:]` is used to remove the '0b' prefix that `bin` adds to the result. 

For example, `rounded_avg(1, 5)` returns `"0b11"`, `rounded_avg(7, 5)` returns -1, `rounded_avg(10, 20)` returns `"0b1111"`, and `rounded_avg(20, 33)` returns `"0b11010"`. 