Here is the solution in Go:

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

This function iterates over the list of integers `l` and checks each value against the threshold `t`. If it finds a value that is greater than or equal to `t`, it immediately returns `false`. If it iterates through the entire list without finding any values that are greater than or equal to `t`, it returns `true`.

Note: In Go, the `range` keyword is used to iterate over arrays, slices, strings, maps, and channels. It returns two values: the index and the value at that index. In this case, we are only interested in the value, so we use `_` as a blank identifier to ignore the index.