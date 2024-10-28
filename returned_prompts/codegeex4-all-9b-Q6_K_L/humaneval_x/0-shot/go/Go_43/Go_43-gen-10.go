```go
func PairsSumToZero(l []int) bool {
    set := make(map[int]bool)
    for _, v := range l {
        if set[-v] {
            return true
        }
        set[v] = true
    }
    return false
}
```
