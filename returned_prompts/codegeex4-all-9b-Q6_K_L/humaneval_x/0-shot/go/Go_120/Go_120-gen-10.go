```go
func Maximum(arr []int, k int) []int {
    sort.Sort(sort.Reverse(sort.IntSlice(arr)))
    return arr[:k]
}
```