    result := make([]string, len(arr))
    for i, v := range arr {
        switch v {
            case 1:
                result[i] = "One"
            case 2:
                result[i] = "Two"
            case 3:
                result[i] = "Three"
            case 4:
                result[i] = "Four"
            case 5:
                result[i] = "Five"
            case 6:
                result[i] = "Six"
            case 7:
                result[i] = "Seven"
            case 8:
                result[i] = "Eight"
            case 9:
                result[i] = "Nine"
            default:
                result[i] = "Ten"
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i] < result[j]
    })
    sort.Slice(result, func(i, j int) bool {
        return result[i] > result[j]
    })
    return result
}



