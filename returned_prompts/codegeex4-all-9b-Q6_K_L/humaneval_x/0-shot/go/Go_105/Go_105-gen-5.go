```go
func ByLength(arr []int)[]string {
    if len(arr) == 0 {
        return []string{}
    }
    var arr2 []int
    for _, v := range arr {
        if v >= 1 && v <= 9 {
            arr2 = append(arr2, v)
        }
    }
    sort.Ints(arr2)
    for i, j := 0, len(arr2)-1; i < j; i, j = i+1, j-1 {
        arr2[i], arr2[j] = arr2[j], arr2[i]
    }
    var result []string
    for _, v := range arr2 {
        switch v {
        case 1:
            result = append(result, "One")
        case 2:
            result = append(result, "Two")
        case 3:
            result = append(result, "Three")
        case 4:
            result = append(result, "Four")
        case 5:
            result = append(result, "Five")
        case 6:
            result = append(result, "Six")
        case 7:
            result = append(result, "Seven")
        case 8:
            result = append(result, "Eight")
        case 9:
            result = append(result, "Nine")
        }
    }
    return result
}
```