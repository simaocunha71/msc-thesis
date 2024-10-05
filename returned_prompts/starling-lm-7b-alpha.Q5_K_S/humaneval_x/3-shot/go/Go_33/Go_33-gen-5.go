    result := make([]int, len(l))
    copy(result, l)

    for i := 0; i < len(l); i++ {
        if i % 3 == 0 {
            index := sort.SearchInts(result[:i], result[i])
            result[i] = result[index]
        }
    }
    return result
}



