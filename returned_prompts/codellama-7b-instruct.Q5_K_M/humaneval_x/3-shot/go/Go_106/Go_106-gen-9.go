    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i%2 == 0 {
            result[i] = 1
            for j := 1; j <= i; j++ {
                result[i] *= j
            }
        } else {
            result[i] = 0
            for j := 1; j <= i; j++ {
                result[i] += j
            }
        }
    }
    return result
}



