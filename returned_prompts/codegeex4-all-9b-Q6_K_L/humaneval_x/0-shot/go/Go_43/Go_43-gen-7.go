```go
func PairsSumToZero(l []int) bool {
    set := make(map[int]bool)
    for _, num := range l {
        if set[-num] {
            return true
        }
        set[num] = true
    }
    return false
}
```
