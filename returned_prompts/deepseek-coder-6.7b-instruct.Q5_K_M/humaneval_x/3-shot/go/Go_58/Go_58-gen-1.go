    common := make([]int, 0)
    m := make(map[int]bool)

    for _, item := range l1  {
        m[item] = true
    }

    for  _, item := range l2  {
        if _, ok := m[item]; ok  {
            common = append(common, item)
        }
    }
    sort.Ints(common)
    return common
}



