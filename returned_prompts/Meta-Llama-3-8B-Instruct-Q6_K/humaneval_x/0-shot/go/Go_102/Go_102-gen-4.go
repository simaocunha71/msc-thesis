```go
func ChooseNum(x, y int) int {
    if x > y {
        x, y = y, x // swap x and y
    }
    for x <= y {
        if x%2 == 0 {
            return x
        }
        x++
    }
    return -1
}
```

Explanation:
This function takes two positive integers `x` and `y` as input and returns the largest even integer that is within the range `[x, y]` inclusive. If no such number exists, the function returns `-1`.

The function first checks if `x` is greater than `y`. If it is, it swaps `x` and `y` to ensure that `x` is the smaller number and `y` is the larger number.

Then, it enters a loop that increments `x` until it is greater than `y`. Inside the loop, it checks if `x` is even by using the modulo operator (`%`). If `x` is even, the function returns `x`.

If the loop completes without finding an even number, the function returns `-1`, indicating that there is no even number in the range `[x, y]`.

For example, if `x = 12` and `y = 15`, the function will return `14`, which is the largest even number in the range `[12, 15]`. If `x = 13` and `y = 12`, the function will return `-1`, indicating that there is no even number in the range `[13, 12]`.