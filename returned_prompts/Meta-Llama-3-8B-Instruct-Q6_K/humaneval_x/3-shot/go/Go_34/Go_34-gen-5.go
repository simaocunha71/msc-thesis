    m := make(map[int]bool)
    result := []int{}
    for _, v := range l {
        if _, value := m[v]; !value {
            m[v] = true
            result = append(result, v)
        }
    }
    sort.Ints(result)
    return result
}