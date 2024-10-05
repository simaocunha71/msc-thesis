    result := make([]int, 0)
    for _, v1 := range l1 {
        for _, v2 := range l2 {
            if v1 == v2 {
                result = append(result, v1)
            }
        }
    }
    sort.Ints(result)
    return result
}



