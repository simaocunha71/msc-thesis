    result := 1
    for i := n; i > 0; i-- {
        result *= math.Factorial(float64(i))
    }
    return int(result)
}
