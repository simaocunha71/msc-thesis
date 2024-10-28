    result := make([]float64, n+1)
    if n < 1 {
        return result
    }
    result[1] = 3.0
    if n == 1 {
        return result
    }
    result[2] = 1.0
    if n == 2 {
        return result
    }
    result[0] = 1.0
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result[i] = 1.0 + float64(i)/2.0
        } else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}