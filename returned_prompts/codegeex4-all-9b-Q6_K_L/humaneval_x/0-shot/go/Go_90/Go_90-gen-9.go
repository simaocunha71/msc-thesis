```go
func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }

    // Sort the list
    sort.Ints(lst)

    // Iterate through the list to find the 2nd smallest element
    for i := 1; i < len(lst); i++ {
        if lst[i] != lst[i-1] {
            return lst[i]
        }
    }

    return nil
}
```
