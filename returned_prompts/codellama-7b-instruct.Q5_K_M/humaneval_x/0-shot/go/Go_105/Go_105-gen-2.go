    for i := 0; i < len(arr); i++ {
        for j := i + 1; j < len(arr); j++ {
            if arr[i] > arr[j] {
                arr[i], arr[j] = arr[j], arr[i]
                goto A
            }
        }
    }
    return arr
}

func IntToStr(arr []int)[]string {
    var res []string
    for _, i := range ByLength(arr) {
        switch i {
        case 1:
            res = append(res, "One")
        case 2:
            res = append(res, "Two")
        case 3:
            res = append(res, "Three")
        case 4:
            res = append(res, "Four")
        case 5:
            res = append(res, "Five")
        case 6:
            res = append(res, "Six")
        case 7:
            res = append(res, "Seven")
        case 8:
            res = append(res, "Eight")
        case 9:
            res = append(res, "Nine")
        default:
            res = append(res, "Zero")
        }
    }
    return res
}

func SortArr(arr []int)[]string {
    sort.Ints(arr)
    return IntToStr(arr)
}
