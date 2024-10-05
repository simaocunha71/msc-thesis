    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    common := make(map[int]bool)

    for _, v := range l1 {
        set1[v] = true
    }
    for _, v := range l2 {
        set2[v] = true
    }

    for k, _ := range set1 {
        if set2[k] {
            common[k] = true
        }
    }

    result := make([]int, 0)
    for k, _ := range common {
        result = append(result, k)
    }
    sort.Ints(result)
    return result
}