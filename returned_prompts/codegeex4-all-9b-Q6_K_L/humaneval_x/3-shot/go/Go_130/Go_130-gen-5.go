    result := make([]float64, 0, n+1)
    result = append(result, 1.0)
    result = append(result, 3.0)
    for i := 2; i <= n; i++ {
        if i % 2 == 0 {
            result = append(result, float64(i)/2)
        } else {
            result = append(result, result[i-1]+result[i-2]+result[i+1])
        }
    }
    return result
}

