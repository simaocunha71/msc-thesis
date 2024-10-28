    result := make([]float64, 0)
    result = append(result, 1)
    result = append(result, 3)
    result = append(result, 2)
    result = append(result, 8)

    for i := 4; i <= n; i++ {
        var next float64
        if i % 2 == 0 {
            next = result[i - 2] + result[i - 1] + result[i - 3]
        }else{
            next = result[i - 1] + result[i - 2] + result[i - 3]
        }
        result = append(result, next)
    }
    return result
}



