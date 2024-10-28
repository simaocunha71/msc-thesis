    result := make([]int, len(l))
    copy(result, l)
    sort.Ints(result[1:len(l):2])
    return result
}



