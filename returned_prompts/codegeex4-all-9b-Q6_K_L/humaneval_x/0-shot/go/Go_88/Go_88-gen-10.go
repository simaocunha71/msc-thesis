```go
func SortArray(array []int) []int {
    result := make([]int, len(array))
    copy(result, array)

    if len(result) == 0 {
        return result
    }

    if (result[0]+result[len(result)-1])%2 == 0 {
        sort.Slice(result, func(i, j int) bool {
            return result[i] > result[j]
        })
    } else {
        sort.Slice(result, func(i, j int) bool {
            return result[i] < result[j]
        })
    }

    return result
}
```
