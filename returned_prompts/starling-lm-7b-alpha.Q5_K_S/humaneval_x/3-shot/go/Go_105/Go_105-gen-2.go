    result := make([]string, 0)
    for _, i := range arr {
        if i >= 1 && i <= 9 {
            result = append(result, i)
        }
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i] < result[j]
    })
    sort.Slice(result, func(i, j int) bool {
        return result[i] > result[j]
    })

    for _, i := range result {
        if i == 1 {
            result = append(result, "One")
        }else if i == 2 {
            result = append(result, "Two")
        }else if i == 3 {
            result = append(result, "Three")
        }else if i == 4 {
            result = append(result, "Four")
        }else if i == 5 {
            result = append(result, "Five")
        }else if i == 6 {
            result = append(result, "Six")
        }else if i == 7 {
            result = append(result, "Seven")
        }else if i == 8 {
            result = append(result, "Eight")
        }else if i == 9 {
            result = append(result, "Nine")
        }
    }

    return result
}



