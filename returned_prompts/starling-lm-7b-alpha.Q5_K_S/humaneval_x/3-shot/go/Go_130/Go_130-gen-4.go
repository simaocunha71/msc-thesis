    result := make([]float64, n + 1)
    result[0] = 3
    result[1] = 1

    for i := 2; i < n + 1; i++ {
        if i % 2 == 0 {
            result[i] = 3
        }else {
            result[i] = result[i-3] + result[i-2] + result[i-1]
        }
    }
    return result
}



