    result := make([]int, 0)
    if n < 2 {
        return result
    }
    for i := 2; i <= n; i++ {
        if n%i == 0 {
            result = append(result, i)
            n = n / i
            i = i - 1
        }
    }
    return result
}



