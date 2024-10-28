```go
func Maximum(arr []int, k int) []int {
    sort.Ints(arr)
    return arr[:k]
}
```

