    if n == 0 {
        return []float64{}
    }
    if n == 1 {
        return []float64{3.0}
    }
    if n == 2 {
        return []float64{3.0, 2.0}
    }

    result := make([]float64, n+1)
    result[0] = 1.0
    result[1] = 3.0
    result[2] = 2.0

    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result[i] = 1.0 + float64(i)/2
        } else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}