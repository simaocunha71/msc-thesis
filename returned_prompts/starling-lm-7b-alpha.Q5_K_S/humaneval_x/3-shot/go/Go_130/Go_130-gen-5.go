    result := make([]float64, n+1)
    result[0] = 3
    result[1] = 1
    result[2] = 1
    for i := 3; i < n + 1; i++ {
        if i % 2 == 0 {
            result[i] = result[i-1] + result[i-2] + result[i-3] + result[i-4]
        }else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}



