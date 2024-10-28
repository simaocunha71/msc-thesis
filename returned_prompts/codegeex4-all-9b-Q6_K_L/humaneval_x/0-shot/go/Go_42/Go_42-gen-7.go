```go
func IncrList(l []int) []int {
    for i, v := range l {
        l[i] = v + 1
    }
    return l
}
```