    m := make(map[int]bool)
    list := []int{}
    for _, item := range l {
        if _, value := m[item]; !value {
            list = append(list, item)
            m[item] = true
        }
    }
    sort.Ints(list)
    return list
}