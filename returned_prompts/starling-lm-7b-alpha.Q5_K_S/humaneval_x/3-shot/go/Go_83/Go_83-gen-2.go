    if n == 1 {
        return 1
    }
    result := 0
    for i := 1; i <= 9; i++ {
        result += math.Pow(10, float64(n-1))
    }
    return result * 2 - 9
}



