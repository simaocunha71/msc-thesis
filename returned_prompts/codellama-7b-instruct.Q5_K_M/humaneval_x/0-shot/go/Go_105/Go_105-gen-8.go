    sort.Ints(arr)
    sort.Reverse(sort.IntSlice(arr))

    names := make([]string, len(arr))
    for i, v := range arr {
        switch v {
        case 1:
            names[i] = "One"
        case 2:
            names[i] = "Two"
        case 3:
            names[i] = "Three"
        case 4:
            names[i] = "Four"
        case 5:
            names[i] = "Five"
        case 6:
            names[i] = "Six"
        case 7:
            names[i] = "Seven"
        case 8:
            names[i] = "Eight"
        case 9:
            names[i] = "Nine"
        }
    }

    return names
}
