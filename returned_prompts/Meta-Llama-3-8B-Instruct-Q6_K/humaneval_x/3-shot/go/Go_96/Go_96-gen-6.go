    result := make([]int, 0)
    for i := 2; i < n; i++ {
        is_prime := true
        for j := 2; j * j <= i; j++ {
            if i % j == 0 {
                is_prime = false
                break
            }
        }
        if is_prime {
            result = append(result, i)
        }
    }
    return result
}