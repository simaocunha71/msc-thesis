    result := make([]float64, n+1)
    result[0] = 1
    result[1] = 3
    result[2] = 2
    result[3] = 8

    for i := 4; i <= n; i++{
        if i%2 == 0 {
            result[i] = result[i / 2] + 2
        }else{
            result[i] = result[i-1] + result[i-2] + result[i+1]
        }
    }

    return result
}



