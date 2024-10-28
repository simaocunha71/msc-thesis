```go
func SortArray(arr []int) []int {
    sort.Slice(arr, func(i, j int) bool {
        countI := 0
        countJ := 0
        for _, v := range fmt.Sprintf("%b", arr[i]) {
            if v == '1' {
                countI++
            }
        }
        for _, v := range fmt.Sprintf("%b", arr[j]) {
            if v == '1' {
                countJ++
            }
        }
        if countI == countJ {
            return arr[i] < arr[j]
        }
        return countI < countJ
    })
    return arr
}
```

