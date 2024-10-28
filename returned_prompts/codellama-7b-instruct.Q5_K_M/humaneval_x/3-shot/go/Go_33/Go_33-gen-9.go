    result := make([]int, len(l))
    copy(result, l)

    sort.Ints(result)

    var i int
    for i = 0; i < len(result); i += 3 {
        if i < len(result) - 2 {
            result[i] = result[i + 2]
            result[i + 2] = result[i + 1]
        }
    }
    return result
}



