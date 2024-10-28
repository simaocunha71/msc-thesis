```go
func SortedListSum(lst []string) []string {
    var out []string
    for _, v := range lst {
        if len(v) % 2 == 0 {
            out = append(out, v)
        }
    }
    sort.Slice(out, func(i, j int) bool {
        if len(out[i]) == len(out[j]) {
            return out[i] < out[j]
        }
        return len(out[i]) < len(out[j])
    })
    return out
}
```