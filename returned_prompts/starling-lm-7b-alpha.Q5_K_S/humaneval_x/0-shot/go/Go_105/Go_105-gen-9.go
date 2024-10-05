    sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })
    sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })
    arr = append(arr[:len(arr)/2], arr[len(arr)/2+1:]...)
    arr = reverse(arr)
    names := []string{}
    for _, v := range arr {
        switch v {
        case 1:
            names = append(names, "One")
        case 2:
            names = append(names, "Two")
        case 3:
            names = append(names, "Three")
        case 4:
            names = append(names, "Four")
        case 5:
            names = append(names, "Five")
        case 6:
            names = append(names, "Six")
        case 7:
            names = append(names, "Seven")
        case 8:
            names = append(names, "Eight")
        case 9:
            names = append(names, "Nine")
        default:
            continue
        }
    }
    return names

func reverse(arr []int) []int {
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
    return arr
}

























































































































































