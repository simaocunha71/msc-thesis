```go
func SortThird(l []int) []int {
    s := make([]int, 0, len(l)/3)
    for i := 2; i < len(l); i += 3 {
        s = append(s, l[i])
    }
    sort.Ints(s)
    j := 0
    for i := 2; i < len(l); i += 3 {
        l[i] = s[j]
        j++
    }
    return l
}
```
