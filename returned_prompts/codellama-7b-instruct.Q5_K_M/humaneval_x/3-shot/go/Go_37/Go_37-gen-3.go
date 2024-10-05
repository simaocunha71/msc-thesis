    result := make([]int, len(l))
    copy(result, l)
    for i := 0; i < len(l); i += 2 {
        sort.Ints(result[i:i+2])
    }
    return result
}



