```go
func PairsSumToZero(l []int) bool {
    if len(l) < 2 {
        return false
    }
    for i := 0; i < len(l)-1; i++ {
        for j := i + 1; j < len(l); j++ {
            if l[i]+l[j] == 0 {
                return true
            }
        }
    }
    return false
}
```