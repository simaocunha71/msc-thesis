    result := make([]int, n)
    for i := range result {
        if n % 2 == 0 {
            result[i] = n + 2*i
        } else {
            result[i] = n + 2*i
        }
    }
    return result
}



