    result := make([]int, 0)

    if n < 2 {
        return result
    }

    result = append(result, 2)

    for i := 3; i <= n; i++ {
        is_prime := true
        for _, p := range result {
            if i % p == 0 {
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



