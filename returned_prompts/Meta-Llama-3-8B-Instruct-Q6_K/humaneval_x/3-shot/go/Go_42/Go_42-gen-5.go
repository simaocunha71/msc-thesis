    result := make([]int, len(l))
    copy(result, l)
    for i := 0; i < len(l); i++ {
        result[i]++
    }
    return result
}