    result := make([]int, len(l))
    copy(result, l)
    for i := range result {
        if i % 3 == 0 {
            result[i] = sort.IntSlice(l).Slice(i, i+1)[:][0]
        }
    }
    return result
}



