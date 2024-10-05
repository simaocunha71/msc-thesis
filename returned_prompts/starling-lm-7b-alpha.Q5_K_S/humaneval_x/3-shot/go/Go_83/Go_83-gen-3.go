    result := 0
    if n == 1 {
        return 1
    }
    for i := 1; i <= 9; i++ {
        result += 1 * pow(10, n - 1) * 9 * math.Pow(10, n - 2)
    }
    for i := 2; i <= 9; i++ {
        result += 1 * pow(10, n - 1) * 9 * math.Pow(10, n - 2)
    }
    return result
}

func pow(base, exponent int) int {
    result := 1
    for i := 0; i < exponent; i++ {
        result *= base
    }
    return result
}




