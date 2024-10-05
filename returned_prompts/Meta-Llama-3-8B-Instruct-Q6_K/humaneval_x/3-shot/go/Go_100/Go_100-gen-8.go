    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = i * 2 + 1
        } else {
            result[i] = i * 2
        }
    }
    return result
}