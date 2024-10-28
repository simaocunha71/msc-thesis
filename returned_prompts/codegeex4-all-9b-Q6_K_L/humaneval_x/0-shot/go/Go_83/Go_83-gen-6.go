Here's how you might do it:

```go
func StartsOneEnds(n int) int {
    if n == 1 {
        return 2
    }
    if n == 2 {
        return 4
    }
    return 18 * int(math.Pow(10, float64(n-2)))
}
```
Explanation:

If `n` is 1 or 2, the function returns 2 or 4 respectively. This is because there are only two 1-digit numbers that start and end with 1: 1 and 0, and four 2-digit numbers that start and end with 1: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19.

For larger `n`, the function uses the formula `18 * 10^(n-2)` to calculate the count. This formula is derived from the fact that for any `n`-digit number, there are 10 possibilities for each of the digits except the first and last (which must be 1), and 18 possibilities for the first and last digits (1 or 2).

Please note that this function assumes that `n` is a positive integer. If `n` can be 0 or negative, additional checks and handling are needed.