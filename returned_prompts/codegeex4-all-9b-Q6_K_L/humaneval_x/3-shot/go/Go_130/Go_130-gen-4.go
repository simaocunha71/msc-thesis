    result := make([]float64, n + 1)
    result[0] = 1
    result[1] = 3
    if n > 1{
        for i := 2; i <= n; i++ {
            if i % 2 == 0{
                result[i] = float64(i / 2)
            }else{
                result[i] = result[i-1] + result[i-2] + result[i-3]
            }
        }
    }
    return result
}



