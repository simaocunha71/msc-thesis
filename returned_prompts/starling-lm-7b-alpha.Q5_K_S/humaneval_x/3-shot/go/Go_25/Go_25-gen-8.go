    result := make([]int, 0)
    for i := 2; i <= n; i++ {
        if n % i == 0 {
            result = append(result, i)
            n /= i
        }
    }
    return result
}



