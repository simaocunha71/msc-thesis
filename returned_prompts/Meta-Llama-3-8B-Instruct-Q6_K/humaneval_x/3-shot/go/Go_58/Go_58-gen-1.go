    m := make(map[int]bool)
    for _, value := range l1 {
        m[value] = true
    }
    var result []int
    for _, value := range l2 {
        if m[value] {
            result = append(result, value)
            delete(m, value)
        }
    }
    sort.Ints(result)
    return result
} 