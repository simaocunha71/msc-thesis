    result := make([]int, 0)
    m := map[int]bool{}
    for _, v := range l1 {
        m[v] = true
    }
    for _, v := range l2 {
        if _, ok := m[v]; ok {
            result = append(result, v)
        }
    }
    sort.Ints(result)
    return result
}



