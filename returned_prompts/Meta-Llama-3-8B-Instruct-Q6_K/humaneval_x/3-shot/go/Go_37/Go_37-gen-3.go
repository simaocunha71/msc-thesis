    result := make([]int, 0, len(l))
    for i := 0; i < len(l); i++ {
        if i % 2 == 0 {
            result = append(result, sort.SearchInts(l, l[i]))
        } else {
            result = append(result, l[i])
        }
    }
    return result
}