```go
func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    unique := make(map[int]bool)
    for _, v := range lst {
        if !unique[v] {
            unique[v] = true
        }
    }
    var smallest []int
    for k := range unique {
        smallest = append(smallest, k)
    }
    if len(smallest) < 2 {
        return nil
    }
    return smallest[1]
}
```