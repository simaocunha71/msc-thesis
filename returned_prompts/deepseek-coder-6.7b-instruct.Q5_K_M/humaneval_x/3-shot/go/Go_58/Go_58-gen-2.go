    m1 := make(map[int]bool)
    for _, item := range l1 {
        m1[item] = true
    }

    common := make([]int, 0)
    for _, item := range l2 {
        if _, ok := m1[item]; ok {
            common = append(common, item)
        }
    }

    sort.Ints(common)
    return common
}



