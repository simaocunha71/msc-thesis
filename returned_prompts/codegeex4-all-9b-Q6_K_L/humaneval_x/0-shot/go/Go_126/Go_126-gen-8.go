```go
func IsSorted(lst []int) bool {
    if len(lst) == 0 {
        return true
    }
    last := lst[0]
    for _, v := range lst[1:] {
        if v < last {
            return false
        }
        if v == last {
            continue
        }
        last = v
    }
    return true
}
```