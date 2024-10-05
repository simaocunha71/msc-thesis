    result := make([]int, len(l))
    copy(result, l)
    sort.Ints(result[1:])

    for i := 0; i < len(result); i += 2 {
        if i+1 < len(result) {
            result[i] = result[i+1]
        }
    }
    return result
}



