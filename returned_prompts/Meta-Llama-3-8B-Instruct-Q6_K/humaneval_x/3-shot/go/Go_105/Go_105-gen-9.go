    var result []string
    var mapping = map[int]string{
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
    sorted := make([]int, 0)
    for _, v := range arr {
        if v >= 1 && v <= 9 {
            sorted = append(sorted, v)
        }
    }
    sort.Ints(sorted)
    sorted = append([]int{}, sorted...)
    sorted = reverse(sorted)
    for _, v := range sorted {
        result = append(result, mapping[v])
    }
    return result
}

func reverse(arr []int) []int {
    var result []int
    for i := len(arr) - 1; i >= 0; i-- {
        result = append(result, arr[i])
    }
    return result
}