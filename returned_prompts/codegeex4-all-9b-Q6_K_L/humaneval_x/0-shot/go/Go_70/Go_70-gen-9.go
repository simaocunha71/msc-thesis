```go
func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return []int{}
    }

    sort.Ints(lst)
    result := make([]int, 0, len(lst))
    for i := 0; i < len(lst); i += 2 {
        result = append(result, lst[i])
        if i+1 < len(lst) {
            result = append(result, lst[len(lst)-1-i])
        }
    }
    return result
}
```