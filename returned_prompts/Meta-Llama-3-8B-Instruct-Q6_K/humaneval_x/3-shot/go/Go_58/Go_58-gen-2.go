    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    for _, value := range l1 {
        set1[value] = true
    }
    for _, value := range l2 {
        set2[value] = true
    }
    common := make([]int, 0)
    for key := range set1 {
        if set2[key] {
            common = append(common, key)
        }
    }
    sort.Ints(common)
    return common
}
