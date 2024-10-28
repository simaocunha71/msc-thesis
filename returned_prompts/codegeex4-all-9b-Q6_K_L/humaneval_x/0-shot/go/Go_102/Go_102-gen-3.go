```go
func ChooseNum(x, y int) int {
    if x > y {
        return -1
    }
    if x%2 == 0 {
        return x
    }
    if y%2 == 0 {
        return y
    }
    if x == y {
        return -1
    }
    return x + 1
}
```

This function checks if `x` is greater than `y`, if so it returns -1. If `x` is even it returns `x`, if `y` is even it returns `y`. If both `x` and `y` are odd and `x` is not equal to `y`, it returns `x + 1`.