    result := make([]int, 0)
    for _, i := range l1 {
        if ContainsInt(l2, i) {
            result = append(result, i)
        }
    }
    sort.Ints(result)
    return result
}



