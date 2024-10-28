    result := make([]int, n)
    for i := 1; i < n; i++ {
        if i%2 == 0 {
            result[i] = i
        } else {
            result[i] = 0
            for j := 1; j <= i; j++ {
                result[i] += j
            }
        }
    }
    return result
}



