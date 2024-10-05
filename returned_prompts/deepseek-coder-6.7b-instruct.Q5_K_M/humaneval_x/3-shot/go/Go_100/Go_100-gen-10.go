    result := make([]int, n)
    for i := range result {
        if n % 2 == 0 {
            result[i] = n + i*2
        } else {
            result[i] = n + i*2
        }
    }
    return result
}



