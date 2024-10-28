```go
func SortThird(l []int) []int {
    temp := make([]int, len(l))
    copy(temp, l)
    sort.Slice(temp[2:], func(i, j int) bool {
        return temp[2+i] < temp[2+j]
    })
    for i := 2; i < len(l); i += 3 {
        l[i] = temp[i]
    }
    return l
}
```