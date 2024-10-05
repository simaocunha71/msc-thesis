    result := make([]float64, n + 1)
    result[0] = 3

    for i := 1; i < n + 1; i++ {
        if i % 2 == 0 {
            result[i] = result[i-1]
        } else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }

    return result
}



