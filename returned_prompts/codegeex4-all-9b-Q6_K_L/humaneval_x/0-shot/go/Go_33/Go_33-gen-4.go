```go
func SortThird(l []int) []int {
    l1 := []int{}
    l2 := []int{}
    for i, v := range l {
        if i%3 == 0 {
            l1 = append(l1, v)
        } else {
            l2 = append(l2, v)
        }
    }
    sort.Ints(l1)
    return append(append(l2[:len(l2)/3], l1...), l2[len(l2)/3:]...)
}
```
