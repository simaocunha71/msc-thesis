    sort.Slice(arr, func(i, j int) bool {
        return arr[i] < arr[j]
    })
    sort.Slice(arr, func(i, j int) bool {
        return arr[i] > arr[j]
    })
    s := make([]string, len(arr))
    for i, v := range arr {
        switch v {
        case 1:
            s[i] = "One"
        case 2:
            s[i] = "Two"
        case 3:
            s[i] = "Three"
        case 4:
            s[i] = "Four"
        case 5:
            s[i] = "Five"
        case 6:
            s[i] = "Six"
        case 7:
            s[i] = "Seven"
        case 8:
            s[i] = "Eight"
        case 9:
            s[i] = "Nine"
        default:
            s[i] = ""
        }
    }
    return s
}























































































































































































































































