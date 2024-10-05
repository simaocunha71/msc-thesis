```go
func BelowThreshold(l []int, t int) bool {
    for _, v := range l {
        if v >= t {
            return false
        }
    }
    return true
}
```

Explanation:
The function `BelowThreshold` takes a slice of integers `l` and an integer `t` as input. It iterates over the slice using a range loop, and for each integer `v` in the slice, it checks if `v` is greater than or equal to `t`. If it finds such a `v`, it immediately returns `false`, indicating that not all numbers in the list are below the threshold. If it iterates over the entire slice without finding any `v` that is greater than or equal to `t`, it returns `true`, indicating that all numbers in the list are below the threshold.