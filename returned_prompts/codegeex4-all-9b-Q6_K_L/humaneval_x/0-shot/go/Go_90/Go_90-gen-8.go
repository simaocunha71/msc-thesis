```go
func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    secondSmallest := lst[1]
    for _, num := range lst {
        if num == secondSmallest {
            return nil
        }
    }
    return secondSmallest
}
```
