    var (
        indexes []int
        ret []string
    )
    for i, v := range arr {
        if v >= 1 && v <= 9 {
            indexes = append(indexes, i)
        }
    }
    sort.Ints(indexes)
    for i := len(indexes) - 1; i >= 0; i-- {
        ret = append(ret, name(arr[indexes[i]]))
    }
    return ret
}

func name(i int) string {
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
    }
    return ""
}

*/

func ByLength(arr []int)[]string {
    var (
        indexes []int
        ret []string
    )
    for i, v := range arr {
        if v >= 1 && v <= 9 {
            indexes = append(indexes, i)
        }
    }
    sort.Ints(indexes)
    for i := len(indexes) - 1; i >= 0; i-- {
        ret = append(ret, name(arr[indexes[i]]))
    }
    return ret
}

func name(i int) string {
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
