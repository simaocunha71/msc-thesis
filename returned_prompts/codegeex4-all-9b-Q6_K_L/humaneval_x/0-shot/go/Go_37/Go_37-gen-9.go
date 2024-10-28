```go
func SortEven(l []int) []int {
    evenIndices := []int{}
    for i := 0; i < len(l); i += 2 {
        evenIndices = append(evenIndices, l[i])
    }
    sort.Ints(evenIndices)
    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        if i%2 == 0 {
            result[i] = evenIndices[i/2]
        } else {
            result[i] = l[i]
        }
    }
    return result
}
```
