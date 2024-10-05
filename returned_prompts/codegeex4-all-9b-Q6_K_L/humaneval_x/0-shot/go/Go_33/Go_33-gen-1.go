```go
func SortThird(l []int) []int {
    sort.Slice(l[2:len(l):2], func(i, j int) bool {
        return l[i*2+2] < l[j*2+2]
    })
    return l
}
```
