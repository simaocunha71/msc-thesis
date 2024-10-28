    m := make(map[int]bool)
    list := []int{}
    for _, item := range l {
        if _, value := m[item]; !value {
            m[item] = true
            list = append(list, item)
        }
    }
    sort.Ints(list)
    return list
}