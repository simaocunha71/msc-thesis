    result := make([]int, len(l))
    copy(result, l)

    for i := 0; i < len(l); i++ {
        if i%3 == 0 {
            result[i] = sort.IntSlice(l[i:]).SortStable().Slice(0, 1)[0]
        }
    }
    return result
}



