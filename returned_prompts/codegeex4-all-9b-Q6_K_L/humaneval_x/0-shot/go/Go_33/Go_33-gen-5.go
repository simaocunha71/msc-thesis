```go
func SortThird(l []int) []int {
    out := make([]int, len(l))
    thirds := []int{}
    for i, v := range l {
        if i%3 == 0 {
            thirds = append(thirds, v)
        }
    }
    sort.Ints(thirds)
    j := 0
    for i, v := range l {
        if i%3 == 0 {
            out[i] = thirds[j]
            j++
        } else {
            out[i] = v
        }
    }
    return out
}
```
