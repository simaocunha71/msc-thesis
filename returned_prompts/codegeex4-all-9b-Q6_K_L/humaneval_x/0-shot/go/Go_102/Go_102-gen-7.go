```go
func ChooseNum(x, y int) int {
    if y < x {
        return -1
    }
    if x%2 == 0 {
        return x
    } else if y%2 == 0 {
        return y
    } else {
        return y - 1
    }
}
```

Explanation:

First, we check if y is less than x. If it is, there is no even number in the range, so we return -1.

Next, we check if x is even. If it is, we return x.

If x is odd, we check if y is even. If it is, we return y.

If neither x nor y is even, we return y - 1. This is because the largest even number in the range [x, y] is either x or y, and if neither of them is even, the largest even number is y - 1.