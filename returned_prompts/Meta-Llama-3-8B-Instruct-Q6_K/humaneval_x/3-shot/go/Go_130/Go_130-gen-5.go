    if n <= 0 {
        return nil
    }
    result := make([]float64, n+1)
    result[0] = 1
    if n >= 1 {
        result[1] = 3
    }
    if n >= 2 {
        result[2] = 1 + 2/2
    }
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result[i] = 1 + float64(i)/2
        } else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}