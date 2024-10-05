    result := make([]int, len(l))
    copy(result, l)
    sort.Slice(result, func(i, j int) bool {
        return result[i] < result[j]
    })
    for i := 0; i < len(l); i++ {
        if i % 3 == 0 {
            result[i] = l[i]
        }
    }
    return result
}



