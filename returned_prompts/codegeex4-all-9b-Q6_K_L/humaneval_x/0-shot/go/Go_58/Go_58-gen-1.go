```go
func Common(l1 []int, l2 []int) []int {
    set := make(map[int]bool)
    for _, num := range l1 {
        set[num] = true
    }
    var common []int
    for _, num := range l2 {
        if set[num] {
            common = append(common, num)
            delete(set, num)
        }
    }
    sort.Ints(common)
    return common
}
```