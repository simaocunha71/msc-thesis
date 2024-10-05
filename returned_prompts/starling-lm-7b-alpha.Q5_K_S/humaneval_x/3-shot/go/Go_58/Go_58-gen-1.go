    l1_set := make(map[int]bool)
    for _, v := range l1 {
        l1_set[v] = true
    }

    result := make([]int, 0)
    for _, v := range l2 {
        if l1_set[v] {
            result = append(result, v)
        }
    }

    sort.Slice(result, func(i, j int) bool {return result[i] < result[j]})
    return result
}



