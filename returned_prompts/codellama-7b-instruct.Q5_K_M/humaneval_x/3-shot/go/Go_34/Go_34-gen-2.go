    sort.Ints(l)
    result := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if i == 0 || l[i] != l[i-1] {
            result = append(result, l[i])
        }
    }
    return result
}



