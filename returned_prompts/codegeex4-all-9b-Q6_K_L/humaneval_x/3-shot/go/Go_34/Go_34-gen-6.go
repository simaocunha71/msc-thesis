    m := make(map[int]bool)
    unique := []int{}
    for _, item := range l {
        if _, ok := m[item]; !ok {
            m[item] = true
            unique = append(unique, item)
        }
    }
    sort.Ints(unique)
    return unique
}

