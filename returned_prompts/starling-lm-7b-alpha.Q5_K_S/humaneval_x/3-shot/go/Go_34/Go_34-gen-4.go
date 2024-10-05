    l = append(l[:0:0], l...)
    sort.Ints(l)
    result := make([]int, 0)
    previous := -1
    for _, v := range l {
        if previous != v {
            result = append(result, v)
        }
        previous = v
    }
    return result
}



