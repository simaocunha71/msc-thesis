    var result []int
    map1 := make(map[int]bool)
    for _, i := range l1 {
        map1[i] = true
    }

    for _, i := range l2 {
        if _, ok := map1[i]; ok {
            result = append(result, i)
        }
    }

    sort.Ints(result)
    return result
}



