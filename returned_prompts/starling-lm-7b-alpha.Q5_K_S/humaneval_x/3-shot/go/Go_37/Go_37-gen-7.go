    result := make([]int, len(l))
    copy(result, l)
    for i := 0; i < len(result); i += 2 {
        sort.Ints(result[i+1:])
    }
    return result
}



