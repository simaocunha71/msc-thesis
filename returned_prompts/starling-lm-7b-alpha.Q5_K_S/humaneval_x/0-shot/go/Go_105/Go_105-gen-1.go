    sort.Ints(arr)
    arr = append(arr[:0], arr[len(arr)-1:]...)
    s := []string{}
    for _, v := range arr {
        switch v {
        case 1: s = append(s, "One")
        case 2: s = append(s, "Two")
        case 3: s = append(s, "Three")
        case 4: s = append(s, "Four")
        case 5: s = append(s, "Five")
        case 6: s = append(s, "Six")
        case 7: s = append(s, "Seven")
        case 8: s = append(s, "Eight")
        case 9: s = append(s, "Nine")
        }
    }
    return s
}



func ByLength(arr []int)[]string {
    sort.Ints(arr)
    arr = append(arr[:0], arr[len(arr)-1:]...)
    s := []string{}
    for _, v := range arr {
        switch v {
        case 1: s = append(s, "One")
        case 2: s = append(s, "Two")
        case 3: s = append(s, "Three")
        case 4: s = append(s, "Four")
        case 5: s = append(s, "Five")
        case 6: s = append(s, "Six")
        case 7: s = append(s, "Seven")
        case 8: s = append(s, "Eight")
        case 9: s = append(s, "Nine")
        }
    }
    return s
}



























































































