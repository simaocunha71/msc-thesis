    result := make([]int, n)
    if n%2 == 0 {
        for i := 0; i < n; i++ {
            result[i] = (i + 1) * 2
        }
    } else {
        for i := 0; i < n; i++ {
            result[i] = (i + 1) * 2 - 1
        }
    }
    return result
}



