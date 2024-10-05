    result := make([]float64, n + 1)
    result[0] = 1
    result[1] = 3
    result[2] = 2

    for i := 3; i < n + 1; i++ {
        if i % 2 == 0 {
            result[i] = (float64(i) / 2.0) + result[i-1]
        }else {
            result[i] = result[i-1] + result[i-2] + result[i+1]
        }
    }
    return result
}



