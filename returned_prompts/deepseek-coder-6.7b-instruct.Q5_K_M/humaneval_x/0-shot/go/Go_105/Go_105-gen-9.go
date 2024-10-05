    sort.Ints(arr)
    var result []string
    for i, _ := range arr {
        switch arr[len(arr)-1-i] {
        case 1:
            result = append(result, "One")
        case 2:
            result =