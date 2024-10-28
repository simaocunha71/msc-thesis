    for _, v := range arr {
        if v < 1 || v > 9 {
            continue A
        }
    }
    sort.Ints(arr)
    sort.Reverse(sort.IntSlice(arr))
    names := make([]string, len(arr))
    for i, v := range arr {
        names[i] = String(v)
    }
    return names
}
