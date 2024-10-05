```go
func ByLength(arr []int)[]string {
    filtered := make([]int, 0)
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filtered = append(filtered, num)
        }
    }

    sort.Ints(filtered)
    for i, j := 0, len(filtered)-1; i < j; i, j = i+1, j-1 {
        filtered[i], filtered[j] = filtered[j], filtered[i]
    }

    return map[int]string{
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }[filtered]
}
```

