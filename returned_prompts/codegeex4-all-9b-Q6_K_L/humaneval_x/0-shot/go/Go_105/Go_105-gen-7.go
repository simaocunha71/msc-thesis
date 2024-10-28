```go
func ByLength(arr []int)[]string {
    // sort the array
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] < arr[j]
    })
    // reverse the array
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
    // map each number to its corresponding name
    names := map[int]string{
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    // filter out numbers not between 1 and 9
    arr = filter(arr)
    // map each number to its name
    result := make([]string, 0, len(arr))
    for _, num := range arr {
        if name, ok := names[num]; ok {
            result = append(result, name)
        }
    }
    return result
}

func filter(arr []int) []int {
    result := make([]int, 0, len(arr))
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            result = append(result, num)
        }
    }
    return result
}
```