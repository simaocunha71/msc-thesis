```go
func StrangeSortList(lst []int) []int {
    if len(lst) == 0 {
        return lst
    }

    sort.Ints(lst)

    result := make([]int, len(lst))
    i, j := 0, len(lst)-1
    for k := 0; k < len(lst); k++ {
        if k%2 == 0 {
            result[k] = lst[i]
            i++
        } else {
            result[k] = lst[j]
            j--
        }
    }

    return result
}
```
