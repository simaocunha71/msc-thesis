    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    result := make([]int, 0)

    for _, v := range l1 {
        set1[v] = true
    }
    for _, v := range l2 {
        if set1[v] {
            result = append(result, v)
            delete(set1, v)
        }
    }
    sort.Ints(result)
    return result
} 





