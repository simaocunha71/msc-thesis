    var result []string
    var sorted_arr []int

    sort.Ints(arr)

    for _, v := range arr {
        if v < 1 || v > 9 {
            continue
        }else{
            sorted_arr = append(sorted_arr, v)
        }
    }

    for _, v := range sorted_arr {
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



