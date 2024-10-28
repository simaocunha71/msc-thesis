    m := make(map[int]bool)
    for _, item := range l1 {
        m[item] = true
    }
    var result []int
    for _, item := range l2 {
        if _, ok := m[item]; ok {
            result = append(result, item)
            m[item] = false
        }
    }
    sort.Ints(result)
    return result
}



