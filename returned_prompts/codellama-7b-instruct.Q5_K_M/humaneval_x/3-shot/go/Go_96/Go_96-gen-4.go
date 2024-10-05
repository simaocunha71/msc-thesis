    result := make([]int, 0)

    for i := 2; i < n; i++ {
        var is_prime bool = true
        for j := 2; j < int(math.Sqrt(float64(i))) + 1; j++ {
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



