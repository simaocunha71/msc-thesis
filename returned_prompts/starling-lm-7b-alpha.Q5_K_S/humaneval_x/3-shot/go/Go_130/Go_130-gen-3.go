    result := make([]float64, n + 1)
    result[0] = 3.0
    result[1] = 1.0
    result[2] = 2.0

    for i := 3; i < len(result); i++ {
        if i % 2 == 0 {
            result[i] = 1 + float64(i) / 2
        }else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}



