    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    intersection := make([]int,0)

    for _, value := range l1 {
        set1[value] = true
    }

    for _, value := range l2 {
        if set1[value] {
            intersection = append(intersection, value)
            delete(set1, value)
        }
        set2[value] = true
    }

    result := make([]int,0)
    for _, value := range intersection {
        result = append(result, value)
    }

    sort.Ints(result)
    return result
}