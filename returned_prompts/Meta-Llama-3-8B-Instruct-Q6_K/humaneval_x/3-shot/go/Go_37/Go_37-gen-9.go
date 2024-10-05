    result := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if i % 2 == 0 {
            result = append(result, sort.Ints(l)[0])
        } else {
            result = append(result, l[i])
        }
    }
    return result
}