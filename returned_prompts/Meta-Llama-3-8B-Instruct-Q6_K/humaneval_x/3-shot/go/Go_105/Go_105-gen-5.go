    var result []string
    filtered := make([]int, 0)
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            filtered = append(filtered, num)
        }
    }
    sort.Ints(filtered)
    for i := len(filtered) - 1; i >= 0; i-- {
        switch filtered[i] {
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