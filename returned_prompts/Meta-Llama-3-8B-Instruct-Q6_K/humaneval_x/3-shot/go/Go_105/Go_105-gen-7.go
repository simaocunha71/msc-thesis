    var result []string
    if len(arr) == 0 {
        return result
    }
    var temp []int
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            temp = append(temp, num)
        }
    }
    sort.Ints(temp)
    temp = append(temp[:0], temp...)
    for _, num := range temp {
        switch num {
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





