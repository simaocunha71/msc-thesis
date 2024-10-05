    result := make([]int, 0)
    m := make(map[int]bool)

    for _, e := range l {
        if _, ok := m[e]; !ok {
            result = append(result, e)
            m[e] = true
        }
    }
    sort.Ints(result)
    return result
}



