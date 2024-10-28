    result := make([]int, 0)
    result = append(result, n)
    for i := 1; i < n; i++ {
        if i%2 == 0 {
            result = append(result, i*2)
        } else {
            result = append(result, i*2+1)
        }
    }
    return result
}



