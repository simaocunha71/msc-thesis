    result := make([]int, n)
    for i := 0; i < n; i++ {
        result[i] = i + 1
    }
    for i := 0; i < n; i++ {
        if result[i] % 2 == 0 {
            result[i] += 1
        }else {
            result[i] += 2
        }
    }
    return result
}



