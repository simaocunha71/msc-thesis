    result := make([]float64, n+1)
    result[0] = 1
    if n > 0 {
        result[1] = 3
        for i := 2; i < n+1; i++ {
            if i % 2 == 0 {
                result[i] = 2 + result[i-1]
            } else {
                result[i] = result[i-1] + result[i-2] + result[i+1]
            }
        }
    }
    return result
}



