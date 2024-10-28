    // sort the array in ascending order
    sort.Ints(arr)

    // reverse the array
    reverse_arr := reverse(arr)

    // replace each digit by its corresponding name
    result := make([]string, len(reverse_arr))
    for i, v := range reverse_arr {
        if v >= 1 && v <= 9 {
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
            }
        }
    }

    return result
}

func reverse(arr []int) []int {
    result := make([]int, len(arr))
    for i, v := range arr {
        result[len(arr)-1-i] = v
    }
    return result
}