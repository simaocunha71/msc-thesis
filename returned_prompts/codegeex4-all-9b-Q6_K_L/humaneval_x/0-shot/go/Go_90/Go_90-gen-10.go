```go
func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    seen := make(map[int]bool)
    for _, num := range lst {
        if !seen[num] {
            seen[num] = true
        }
    }
    var result []int
    for num := range seen {
        result = append(result, num)
    }
    if len(result) < 2 {
        return nil
    }
    return result[1]
}
```