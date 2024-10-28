```go
func SortThird(l []int) []int {
    sortedThird := make([]int, len(l))
    for i, x := range l {
        if i%3 == 0 {
            sortedThird[i] = x
        }
    }
    sort.Ints(sortedThird)
    for i, x := range sortedThird {
        if i%3 == 0 {
            l[i] = x
        }
    }
    return l
}
```