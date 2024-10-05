    result := make([]int, 0)

    for _, v := range l1 {
        if sort.SearchInts(l2, v) != len(l2) {
            result = append(result, v)
        }
    }
    return result
}



