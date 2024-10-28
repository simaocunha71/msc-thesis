    result := make([]int, n)
    current := 1
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = current
            current += 2
        }else{
            result[i] = current
            current += 1
        }
    }
    return result
}