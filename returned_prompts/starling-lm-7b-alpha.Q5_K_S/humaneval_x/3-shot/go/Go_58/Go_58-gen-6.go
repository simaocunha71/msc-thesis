    m1 := make(map[int]struct{})
    for _, v := range l1 {
        m1[v] = struct{}{}
    }
    m2 := make(map[int]struct{})
    for _, v := range l2 {
        m2[v] = struct{}{}
    }
    result := make([]int, 0)
    for k := range m1 {
        if _, ok := m2[k]; ok {
            result = append(result, k)
        }
    }
    sort.Ints(result)
    return result
}



