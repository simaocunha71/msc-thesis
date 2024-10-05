```go
func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    for i, v := range lst {
        if i == 0 {
            if v == lst[i+1] {
                return nil
            }
        } else if i == len(lst)-1 {
            if v == lst[i-1] {
                return nil
            }
        } else {
            if v != lst[i-1] && v != lst[i+1] {
                return v
            }
        }
    }
    return nil
}
```