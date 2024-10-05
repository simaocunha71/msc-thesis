    result := make([]string,0)

    for _, num := range arr{
        if num >= 1 && num <= 9 {
            result = append(result, numToString(num))
        }
    }

    sort.Ints(arr)

    for i, j := 0, len(arr) - 1; i < j; i, j = i + 1, j - 1 {
        arr[i], arr[j] = arr[j], arr[i]
    }

    for _, num := range arr{
        if num >= 1 && num <= 9 {
            result = append(result, numToString(num))
        }
    }

    return result
}

func numToString(num int) string{
    switch num {
    case 1:
        return "One"
    case 2:
        return "Two"
    case 3:
        return "Three"
    case 4:
        return "Four"
    case 5:
        return "Five"
    case 6:
        return "Six"
    case 7:
        return "Seven"
    case 8:
        return "Eight"
    case 9:
        return "Nine"
    default:
        return ""
    }
}



