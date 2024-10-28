    result := 1
    for i := 1; i <= n; i++ {
        result *= math.Factorial(float64(i))
    }
    return int(result)
}