    var result []string
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] < arr[j]
    })
    for _, v := range arr {
        if v < 10 {
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
    }
    return result
}