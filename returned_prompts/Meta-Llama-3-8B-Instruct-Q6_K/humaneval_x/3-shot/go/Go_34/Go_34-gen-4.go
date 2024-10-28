    m := make(map[int]bool)
    result := make([]int, 0)
    for _, val := range l {
        if _, value := m[val]; !value {
            m[val] = true
            result = append(result, val)
        }
    }
    sort.Ints(result)
    return result
}