    factors := make([]int, 0)
    for i := 2; i <= n; i++ {
        if n%i == 0 {
            factors = append(factors, i)
        }
    }
    return factors
}

