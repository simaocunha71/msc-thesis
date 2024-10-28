    if n==0{
        return make([]float64,0)
    }
    result := make([]float64, n+1)
    result[0] = 3
    result[1] = 1
    result[2] = 2
    for i := 3; i <= n; i++ {
        if i%2==0 {
            result[i] = result[i-1] + result[i-2] + result[i-3] + 1
        }else {
            result[i] = result[i-2] + result[i-1] + result[i+1] + 1
        }
    }
    return result
}



