    result := make([]int, len(l))
    for i := 0; i < len(l); i++ {
        result[i] = l[i]
    }
    sort.Slice(result[0:len(l):2], func(i int, j int) bool {
        return result[i] < result[j]
    })
    return result
}



