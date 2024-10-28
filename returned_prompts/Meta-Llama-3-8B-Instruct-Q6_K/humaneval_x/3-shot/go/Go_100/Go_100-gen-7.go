    result := make([]int, n)
    result[0] = n
    for i := 1; i < n; i++ {
        if i % 2 == 0 {
            result[i] = i * 2
        } else {
            result[i] = i * 2 + 1
        }
    }
    return result
}