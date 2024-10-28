    result := make([]int, len(l))
    copy(result, l)

    sort.Ints(result[1::2])

    return result
}