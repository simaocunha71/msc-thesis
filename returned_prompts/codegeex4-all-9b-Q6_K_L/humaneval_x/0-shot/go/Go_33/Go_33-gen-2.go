```go
func SortThird(l []int) []int {
    sorted := make([]int, len(l))
    copy(sorted, l)
    for i := 0; i < len(sorted); i += 3 {
        sort.Ints(sorted[i : i+3])
    }
    return sorted
}
```
