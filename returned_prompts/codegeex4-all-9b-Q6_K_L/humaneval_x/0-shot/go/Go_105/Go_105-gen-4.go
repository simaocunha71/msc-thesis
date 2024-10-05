```go
func ByLength(arr []int) []string {
    digits := map[int]string{1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    var result []string
    for _, v := range arr {
        if v >= 1 && v <= 9 {
            result = append(result, digits[v])
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return len(result[i]) > len(result[j])
    })
    reverse(result)
    return result
}

func reverse(arr []string) {
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
}
```