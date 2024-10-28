    result := make([]int, n)
    count := 1
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = count
            count += 2
        } else {
            result[i] = count
            count += 1
        }
    }
    return result
}