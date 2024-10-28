    result := make([]float64, 0)

    if n == 0 {
        result = append(result, 3)
        return result
    }

    result = append(result, 1, 3)
    for i := 2; i < n; i++ {
        if i%2 == 0 {
            result = append(result, 1.0+(float64(i)/2.0))
        } else {
            result = append(result, result[i-1]+result[i-2]+result[i-3])
        }
    }

    return result
}