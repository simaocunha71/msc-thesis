    result := make([]int, 0)
    for i := 0; i < len(l); i++ {
        if l[i] > 0 {
            result = append(result, l[i])
        }
    }
    return result
}



