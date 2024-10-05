    result := make([]int, len(l))
    copy(result, l)

    for i := 0; i < len(result); i++ {
        if i % 3 == 0 {
            result[i] = sort.IntSlice(result[i:]).SortStable()
        }
    }
    return result
}



