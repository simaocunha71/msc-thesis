    m := make(map[int]bool)
    for _, item := range l1 {
        m[item] = true
    }

    common := make([]int, 0)
    for _, item := range l2 {
        if _, ok := m[item]; ok {
            // ensures the common elements are unique
            delete(m, item)
            common = append(common, item)
        }
    }
    sort.Ints(common)
    return common
}



