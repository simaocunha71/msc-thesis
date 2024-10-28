    result := make([]int, len(lst))
    copy(result, lst)
    sort.Slice(result, func(i, j int) bool {
        return result[i] <= result[j]
    })
    for i := 0; i < len(result); i++ {
        if i % 2 == 1 {
            result[i], result[0] = result[0], result[i]
            break
        }
    }
    return result
}



