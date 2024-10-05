    result := 1
    for i := 1; i <= n; i++ {
        factor := 1
        for j := 1; j <= i; j++ {
            factor *= j
        }
        result *= factor
    }
    return result
}