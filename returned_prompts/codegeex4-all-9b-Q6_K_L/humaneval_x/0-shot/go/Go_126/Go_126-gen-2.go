```go
func IsSorted(lst []int) bool {
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] >= lst[i+1] {
            return false
        }
    }
    return true
}
```