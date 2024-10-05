    result := make([]string, 0)
    numbers := make([]int, 0)

    for _, e := range arr {
        if e >= 1 && e <= 9 {
            numbers = append(numbers, e)
        }
    }
    sort.Ints(numbers)
    for i := len(numbers)-1; i >= 0; i-- {
        result = append(result, numberToWord(numbers[i]))
    }

    return result
}

func numberToWord(i int) string {
    switch i {
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

