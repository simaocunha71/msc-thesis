Here is the solution in Go:

```go
func ChooseNum(x, y int) int {
    if x > y {
        return -1
    }

    if x%2 == 0 {
        return x
    }

    if x == y {
        return -1
    }

    return x + 1
}
```

Explanation:
- First, we check if `x` is greater than `y`. If it is, there is no even number in the range `[x, y]`, so we return `-1`.
- Then, we check if `x` is even. If it is, we return `x` because it is the biggest even number in the range `[x, y]`.
- If `x` is odd, we check if `x` is equal to `y`. If it is, there is no even number in the range `[x, y]`, so we return `-1`.
- If `x` is odd and not equal to `y`, we return `x + 1` because it is the biggest even number in the range `[x, y]`.

Note: This solution assumes that `x` and `y` are positive integers. If `x` or `y` can be negative or zero, additional checks need to be added.