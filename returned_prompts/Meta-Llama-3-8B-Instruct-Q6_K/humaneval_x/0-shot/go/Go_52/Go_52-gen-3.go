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


This function uses a for loop to iterate over the slice of integers `l`. For each integer `v` in the slice, it checks if `v` is greater than or equal to the threshold `t`. If it finds such an integer, it immediately returns `false`. If it doesn't find any integers greater than or equal to `t`, it returns `true` after the loop finishes. This is because the `return` statement inside the loop short-circuits the function, so the function returns as soon as it finds an integer that is not below the threshold. The function returns `true` only if all integers in the slice are below the threshold.