    if n == 0 {
        return []float64{}
    }
    result := make([]float64, n + 1)
    result[0] = float64(3)
    result[1] = float64(1)
    if n % 2 == 0 {
        for i := 2; i <= n; i += 2 {
            result[i] = result[i - 2] + float64(1) + result[i - 1]
        }
    }else {
        for i := 2; i <= n; i += 2 {
            result[i] = result[i - 1] + result[i - 2] + result[i + 1]
        }
    }
    return result
}



