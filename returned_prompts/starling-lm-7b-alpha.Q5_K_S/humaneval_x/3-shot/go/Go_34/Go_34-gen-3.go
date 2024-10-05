    result := make([]int, 0)
    unique := make(map[int]bool)
    for _, v := range l {
        if _, ok := unique[v]; !ok {
            unique[v] = true
            result = append(result, v)
        }
    }
    sort.Ints(result)
    return result
}



