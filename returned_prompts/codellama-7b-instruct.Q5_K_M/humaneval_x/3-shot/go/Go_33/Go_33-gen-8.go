    result := make([]int, len(l))
    copy(result, l)

    sort.SliceStable(result, func(i, j int) bool {
        if i % 3 == j % 3 {
            return false
        }
        return i % 3 < j % 3
    })
    return result
}



