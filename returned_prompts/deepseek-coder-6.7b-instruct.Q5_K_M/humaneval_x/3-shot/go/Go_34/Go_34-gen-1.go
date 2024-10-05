    unique := make(map[int]bool)
    for _, item := range l {
        unique[item] = true
    }

    result := make([]int, len(unique))
    i := 0
    for key := range unique {
        result[i] = key
        i++
    }
    sort.Ints(result)
    return result
}

