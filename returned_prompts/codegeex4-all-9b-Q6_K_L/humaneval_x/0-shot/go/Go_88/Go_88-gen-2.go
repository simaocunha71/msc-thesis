```go
func SortArray(array []int) []int {
    copyArray := make([]int, len(array))
    copy(copyArray, array)
    sort.Slice(copyArray, func(i, j int) bool {
        if (copyArray[i]+copyArray[j])%2 == 0 {
            return copyArray[i] > copyArray[j]
        }
        return copyArray[i] < copyArray[j]
    })
    return copyArray
}
```
