```go
func IncrList(l []int) []int {
    for i := range l {
        l[i]++
    }
    return l
}
```