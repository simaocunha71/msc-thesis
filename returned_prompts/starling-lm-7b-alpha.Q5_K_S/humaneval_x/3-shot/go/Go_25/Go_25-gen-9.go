    result := make([]int, 0)
    for i := 2; i*i <= n; i++ {
        while n % i == 0 {
            result = append(result, i)
            n = n / i
        }
    }
    if n > 1 {
        result = append(result, n)
    }
    return result
}



