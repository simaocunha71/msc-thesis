    result := make([]int, len(lst))
    copy(result, lst)
    sort.Slice(result, func(i, j int) bool {
        return result[i] < result[j]
    })
    for i := 0; i < len(result)/2; i++ {
        result[i], result[len(result)-1-i] = result[len(result)-1-i], result[i]
    }
    return result
}



