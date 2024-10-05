    result := make([]int, len(l))
    copy(result, l)
    sort.Slice(result[:], func(i, j int) bool {
        return result[i]%3 < result[j]%3
    })
    return result
}



