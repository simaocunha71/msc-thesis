Here is a simple implementation in Go:
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
This function iterates over the slice `l` and checks if any value is greater than or equal to the threshold `t`. If it finds such a value, it immediately returns `false`. If it checks all values and doesn't find any that exceed the threshold, it returns `true`.